import os

# 🔧 Set your folder path below
directory = r" PUT HERE YOUR DIRECTORY "

# Get all files in the folder
files = os.listdir(directory)

# Separate video and subtitle files
videos = sorted([f for f in files if f.lower().endswith('.mkv')])
subs = sorted([f for f in files if f.lower().endswith('.srt')])

# Check if counts match
if len(videos) != len(subs):
    print(f"⚠️ Warning: {len(videos)} video(s) and {len(subs)} subtitle(s) found.")
    print("The script will rename subtitles in order of appearance.\n")

# Rename subtitles to match video filenames (same base name, .srt extension)
for i in range(min(len(videos), len(subs))):
    video = videos[i]
    sub = subs[i]

    new_sub_name = os.path.splitext(video)[0] + '.srt'

    old_path = os.path.join(directory, sub)
    new_path = os.path.join(directory, new_sub_name)

    os.rename(old_path, new_path)
    print(f"✅ Renamed '{sub}' → '{new_sub_name}'")
