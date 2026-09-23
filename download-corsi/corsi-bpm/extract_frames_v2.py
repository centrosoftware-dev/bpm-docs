import re, sys, os, subprocess

def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')[:50]

def ts_to_seconds(ts):
    h, m, s = ts.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def main(course_dir, start_idx=1, end_idx=None):
    md_path = os.path.join(course_dir, "timestamps.md")
    video_path = os.path.join(course_dir, "course.mkv")
    frames_dir = os.path.join(course_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    rows = []
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r'\|\s*\[(\d{2}:\d{2}:\d{2})\]\s*\|\s*([^|]+)\|\s*([^|]+)\|', line)
            if m:
                ts, category, title = m.group(1), m.group(2).strip(), m.group(3).strip()
                rows.append((ts, category, title))

    if end_idx is None:
        end_idx = len(rows)

    log_path = os.path.join(course_dir, "frames_manifest.csv")
    write_header = not os.path.exists(log_path)
    with open(log_path, "a", encoding="utf-8") as logf:
        if write_header:
            logf.write("index,timestamp,category,title,filename,extracted_at_seconds,shift_seconds\n")
        for i, (ts, category, title) in enumerate(rows, 1):
            if i < start_idx or i > end_idx:
                continue
            secs = ts_to_seconds(ts)
            if i < len(rows):
                next_secs = ts_to_seconds(rows[i][0])  # rows[i] is next row (0-indexed vs 1-indexed i)
            else:
                next_secs = secs + 200
            gap = max(0, next_secs - secs)
            shift = min(90, max(0, gap * 0.4))
            target = secs + shift

            # filename keeps the ORIGINAL nominal timestamp for naming consistency with existing docs
            fname = f"{i:03d}_{ts.replace(':','')}_{slugify(title)}.jpg"
            out_path = os.path.join(frames_dir, fname)
            cmd = [
                "ffmpeg", "-y", "-ss", str(target), "-i", video_path,
                "-frames:v", "1", "-q:v", "3", out_path
            ]
            r = subprocess.run(cmd, capture_output=True, text=True)
            ok = os.path.exists(out_path) and os.path.getsize(out_path) > 0
            print(f"[{i}/{len(rows)}] nominal={ts} shift=+{shift:.0f}s -> extracted_at={target:.0f}s -> {fname} {'OK' if ok else 'FAILED'}", flush=True)
            logf.write(f"{i},{ts},{category},{title},{fname},{target:.0f},{shift:.0f}\n")
            logf.flush()

if __name__ == "__main__":
    course_dir = sys.argv[1]
    start_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_idx = int(sys.argv[3]) if len(sys.argv) > 3 else None
    main(course_dir, start_idx, end_idx)
