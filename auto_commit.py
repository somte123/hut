import os
import subprocess
import datetime

# --- CONFIG ---
REPO_PATH = r"C:\users\user\Desktop\generalfolder\amara"
DUMMY_FILE = "auto_log.txt"
TOTAL_COMMITS = 2229
COMMITS_PER_PUSH = 100
GIT_NAME =  "obi1990-tech"                         
GIT_EMAIL =  "aobi7496@gmail.com"

# ---------------

os.chdir(REPO_PATH)

# Ensure correct git identity is set
subprocess.run(["git", "config", "user.name", GIT_NAME])
subprocess.run(["git", "config", "user.email", GIT_EMAIL])

print("🚀 Starting auto commits...")

for i in range(1, TOTAL_COMMITS + 1):
    with open(DUMMY_FILE, "a") as f:
        f.write(f"Commit #{i} - {datetime.datetime.now()}\n")

    subprocess.run(["git", "add", DUMMY_FILE], check=True)
    subprocess.run(["git", "commit", "-m", f"Auto Commit #{i}"], check=True)

    if i % COMMITS_PER_PUSH == 0 or i == TOTAL_COMMITS:
        print(f"📤 Pushing at commit #{i}...")
        subprocess.run(["git", "push", "origin", "main"], check=True)

print("✅ Done! All commits made and pushed.")