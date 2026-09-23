import re, subprocess, os, sys

course = sys.argv[1]
video_duration = float(sys.argv[2])
manifest_path = f"{course}/frames_manifest.csv"

line_re = re.compile(r'^(\d+),(\d{2}:\d{2}:\d{2}),([^,]+),(.*),(\d{3}_\d{6}_[a-z0-9-]+\.jpg),(\d+),(\d+)$')

rows = []
with open(manifest_path, encoding='utf-8') as f:
    next(f)  # header
    for line in f:
        line = line.rstrip('\n')
        m = line_re.match(line)
        if not m:
            print("UNPARSED:", line)
            continue
        idx, ts, cat, title, filename, ext_s, shift_s = m.groups()
        rows.append({'index': int(idx), 'timestamp': ts, 'title': title, 'filename': filename})

rows.sort(key=lambda r: r['index'])
print(f"parsed {len(rows)} rows total")

def to_seconds(ts):
    h, m, s = map(int, ts.split(':'))
    return h*3600 + m*60 + s

# cross-check against the old (buggy) candidates dir: which stems are missing?
existing_stems = set()
for fn in os.listdir(f"{course}/candidates"):
    m = re.match(r'^(.*)__c\d_t\d+\.jpg$', fn)
    if m:
        existing_stems.add(m.group(1))

os.makedirs(f"{course}/candidates", exist_ok=True)
N = 6
video = f"{course}/course.mkv"
fixed = []
for i, row in enumerate(rows):
    stem = row['filename'][:-4]
    if stem in existing_stems:
        continue
    fixed.append(row['index'])
    t0 = to_seconds(row['timestamp'])
    if i + 1 < len(rows):
        t1 = min(to_seconds(rows[i+1]['timestamp']) - 2, t0 + 120)
    else:
        t1 = min(video_duration - 2, t0 + 120)
    if t1 <= t0:
        t1 = t0 + 5
    span = t1 - t0
    for k in range(N):
        t = t0 + (span * k / (N - 1) if span > 0 else 0)
        out = f"{course}/candidates/{stem}__c{k}_t{int(t)}.jpg"
        subprocess.run(["ffmpeg", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", "-q:v", "3", out],
                        capture_output=True)
    print(f"FIXED {row['index']}: {row['title']} -> window [{t0},{t1}] stem={stem}")

print("missing/fixed indices:", fixed)
