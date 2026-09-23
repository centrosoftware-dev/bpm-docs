import re, json, sys

course = sys.argv[1]
video_duration = float(sys.argv[2])
manifest_path = f"{course}/frames_manifest.csv"
line_re = re.compile(r'^(\d+),(\d{2}:\d{2}:\d{2}),([^,]+),(.*),(\d{3}_\d{6}_[a-z0-9-]+\.jpg),(\d+),(\d+)$')

rows = []
with open(manifest_path, encoding='utf-8') as f:
    next(f)
    for line in f:
        line = line.rstrip('\n')
        m = line_re.match(line)
        idx, ts, cat, title, filename, ext_s, shift_s = m.groups()
        rows.append({'index': int(idx), 'timestamp': ts, 'category': cat, 'title': title, 'filename': filename})

rows.sort(key=lambda r: r['index'])

def to_seconds(ts):
    h, m, s = map(int, ts.split(':'))
    return h*3600 + m*60 + s

for i, row in enumerate(rows):
    t0 = to_seconds(row['timestamp'])
    if i + 1 < len(rows):
        t1 = min(to_seconds(rows[i+1]['timestamp']) - 2, t0 + 120)
    else:
        t1 = min(video_duration - 2, t0 + 120)
    if t1 <= t0:
        t1 = t0 + 5
    row['t0'] = t0
    row['t1'] = t1
    row['stem'] = row['filename'][:-4]

with open(f"{course}/clean_manifest.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print(f"{course}: wrote {len(rows)} rows")
