import csv, subprocess, os, sys

course = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
video_duration = float(sys.argv[4])

manifest_path = f"{course}/frames_manifest.csv"
rows = list(csv.DictReader(open(manifest_path, encoding="utf-8")))

def to_seconds(ts):
    h, m, s = map(int, ts.split(':'))
    return h*3600 + m*60 + s

os.makedirs(f"{course}/candidates", exist_ok=True)

N = 6
video = f"{course}/course.mkv"
done = 0
for i, row in enumerate(rows):
    idx = int(row['index'])
    if idx < start or idx > end:
        continue
    t0 = to_seconds(row['timestamp'])
    if i + 1 < len(rows):
        t_next = to_seconds(rows[i+1]['timestamp'])
        t1 = min(t_next - 2, t0 + 120)
    else:
        t1 = min(video_duration - 2, t0 + 120)
    if t1 <= t0:
        t1 = t0 + 5
    span = t1 - t0
    stem = row['filename'][:-4]
    for k in range(N):
        t = t0 + (span * k / (N - 1) if span > 0 else 0)
        out = f"{course}/candidates/{stem}__c{k}_t{int(t)}.jpg"
        subprocess.run(["ffmpeg", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", "-q:v", "3", out],
                        capture_output=True)
    done += 1
    print(f"{idx}: {row['title']} -> window [{t0},{t1}]")
print(f"DONE chunk {start}-{end}: {done} items")
