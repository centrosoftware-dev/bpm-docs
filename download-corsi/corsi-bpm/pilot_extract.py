import subprocess, os

# (label, course_dir, video_rel, ts_start, ts_end, title)
items = [
    ("base_1", "bpm-base", 677, 797, "Process variables (magazzino)"),
    ("base_2", "bpm-base", 6778, 6898, "The formula editor (Visual Basic)"),
    ("base_3", "bpm-base", 8954, 9074, "Conditions drive approval branching"),
    ("base_4", "bpm-base", 12756, 12876, "Group (master-detail) variables"),
    ("base_5", "bpm-base", 18325, 18423, "Permission baseline: citation is enough"),
    ("avz_6", "bpm-avanzato", 2055, 2175, "VB-script loop over group rows"),
    ("avz_7", "bpm-avanzato", 5024, 5144, "Attesa (wait) event [definition]"),
    ("avz_8", "bpm-avanzato", 8439, 8559, "Decision table demo: amount to approver"),
    ("avz_9", "bpm-avanzato", 11452, 11572, "Connettore attivo (active connector) operation"),
    ("avz_10", "bpm-avanzato", 18276, 18309, "Real project: coffee-roasting dashboard [anecdote]"),
]

N = 6
for label, course, t0, t1, title in items:
    video = os.path.join(course, "course.mkv")
    span = t1 - t0
    for k in range(N):
        t = t0 + (span * k / (N - 1) if span > 0 else 0)
        out = f"pilot/{label}_c{k}_t{int(t)}.jpg"
        subprocess.run(["ffmpeg","-y","-ss",str(t),"-i",video,"-frames:v","1","-q:v","3",out],
                        capture_output=True)
    print(f"{label}: {title} -> window [{t0},{t1}] ({N} candidates)")
