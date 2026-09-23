#!/usr/bin/env python3
"""
Trascrizione dei corsi (bpm-base, bpm-avanzato) via Azure OpenAI Whisper.

USO:
  1. pip install requests   (se non già installato)
  2. imposta la tua chiave come variabile d'ambiente:
       PowerShell:  $env:AZURE_WHISPER_KEY = "la-tua-chiave"
       cmd:         set AZURE_WHISPER_KEY=la-tua-chiave
  3. esegui questo script dalla cartella download-corsi (o passa il path):
       python transcribe.py

Rispetta un rate limit di 3 richieste/minuto (endpoint Azure) ed è
RIPRENDIBILE: se lo interrompi e lo rilanci, salta i chunk già fatti.

I timestamp assoluti (riferiti all'intero video originale, non al singolo
chunk) vengono calcolati sommando l'offset del chunk (indice * durata
chunk) al timestamp restituito da Whisper per quel chunk — così ogni
segmento di trascrizione resta ancorato al punto esatto nel video, e
possiamo poi usarlo per estrarre lo screenshot corrispondente con ffmpeg.
"""

import os
import sys
import json
import time
import glob

try:
    import requests
except ImportError:
    print("Manca il pacchetto 'requests'. Installalo con: pip install requests")
    sys.exit(1)

# --- Configurazione ---------------------------------------------------

ENDPOINT_BASE = "https://cs-test.openai.azure.com/openai/deployments/whisper/audio/transcriptions"
API_VERSION = "2024-06-01"
API_KEY = "b859ff1fb8da4542b7b0fa2d3e7e88a0"

CHUNK_SECONDS = 1200  # deve combaciare con -segment_time usato per creare i chunk
MIN_INTERVAL = 21     # secondi tra una richiesta e l'altra (limite: 3/min = 20s min + margine)
LANGUAGE = "it"

COURSES = ["bpm-base", "bpm-avanzato"]

# -----------------------------------------------------------------------


def transcribe_chunk(path, max_retries=5):
    url = f"{ENDPOINT_BASE}?api-version={API_VERSION}"
    headers = {"api-key": API_KEY}
    for attempt in range(max_retries):
        with open(path, "rb") as f:
            files = {"file": (os.path.basename(path), f, "audio/mpeg")}
            data = {"response_format": "verbose_json", "language": LANGUAGE}
            resp = requests.post(url, headers=headers, files=files, data=data, timeout=300)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", "30"))
            print(f"  Rate limited (429), aspetto {retry_after}s...")
            time.sleep(retry_after)
            continue
        print(f"  Errore {resp.status_code}: {resp.text[:300]}")
        time.sleep(10)
    raise RuntimeError(f"Fallito dopo {max_retries} tentativi: {path}")


def process_course(course_dir):
    chunks_dir = os.path.join(course_dir, "chunks")
    chunk_files = sorted(glob.glob(os.path.join(chunks_dir, "chunk_*.mp3")))
    if not chunk_files:
        print(f"Nessun chunk trovato in {chunks_dir}, salto.")
        return

    out_json_path = os.path.join(course_dir, "transcript.json")
    out_txt_path = os.path.join(course_dir, "transcript.txt")

    all_segments = []
    done_chunks = set()
    if os.path.exists(out_json_path):
        with open(out_json_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
            all_segments = existing.get("segments", [])
            done_chunks = set(existing.get("done_chunks", []))

    print(f"\n=== {os.path.basename(course_dir)} — {len(chunk_files)} chunk totali, {len(done_chunks)} già fatti ===")

    for idx, chunk_path in enumerate(chunk_files):
        chunk_name = os.path.basename(chunk_path)
        if chunk_name in done_chunks:
            continue

        offset = idx * CHUNK_SECONDS
        print(f"[{idx + 1}/{len(chunk_files)}] {chunk_name} (offset {offset}s) ...", flush=True)

        result = transcribe_chunk(chunk_path)

        for seg in result.get("segments", []):
            all_segments.append({
                "start": round(seg["start"] + offset, 2),
                "end": round(seg["end"] + offset, 2),
                "text": seg["text"].strip(),
            })

        done_chunks.add(chunk_name)

        # salvataggio progressivo: se lo interrompi, riparte da qui
        with open(out_json_path, "w", encoding="utf-8") as f:
            json.dump(
                {"segments": all_segments, "done_chunks": sorted(done_chunks)},
                f, ensure_ascii=False, indent=2,
            )

        time.sleep(MIN_INTERVAL)

    all_segments.sort(key=lambda s: s["start"])
    with open(out_txt_path, "w", encoding="utf-8") as f:
        for seg in all_segments:
            h = int(seg["start"] // 3600)
            m = int((seg["start"] % 3600) // 60)
            s = int(seg["start"] % 60)
            f.write(f"[{h:02d}:{m:02d}:{s:02d}] {seg['text']}\n")

    print(f"Completato: {out_json_path}")
    print(f"Completato: {out_txt_path}")


def main():
    if not API_KEY:
        print("ERRORE: imposta la variabile d'ambiente AZURE_WHISPER_KEY con la tua chiave API prima di lanciare lo script.")
        sys.exit(1)

    base_dir = os.path.dirname(os.path.abspath(__file__))

    for course in COURSES:
        course_dir = os.path.join(base_dir, course)
        if not os.path.isdir(course_dir):
            print(f"Cartella non trovata: {course_dir}, salto.")
            continue
        process_course(course_dir)

    print("\nTutto completato.")


if __name__ == "__main__":
    main()
