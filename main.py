import os
import shutil

desktop = input("Enter Path")

listAA = os.listdir(desktop)

for app in listAA:

    source = os.path.join(desktop, app)

    # Skip folders
    if os.path.isdir(source):
        continue

    if app.lower().endswith((".mkv", ".mp4")):
        folder = os.path.join(desktop, "videos")

    elif app.lower().endswith((".lnk", ".url")):
        folder = os.path.join(desktop, "Apps")

    elif app.lower().endswith((".pdf", ".docx", ".py", ".webp", ".bat")):
        folder = os.path.join(desktop, "Files")

    elif app.lower().endswith((".png", ".jpg", ".jpeg", ".avif")):
        folder = os.path.join(desktop, "Photos")

    elif app.lower().endswith((".mp3", ".wav", ".flac", ".m4a")):
        folder = os.path.join(desktop, "Audio")

    else:
        folder = os.path.join(desktop, "Others")

    os.makedirs(folder, exist_ok=True)

    destination = os.path.join(folder, app)

    try:
        shutil.move(source, destination)
        print(f"Moved: {app} -> {os.path.basename(folder)}")

    except Exception as e:
        print(f"Could not move {app}: {e}")