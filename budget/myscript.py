import os
import subprocess
import sys
result = subprocess.run(["python", "manage.py", "test"], check=False)

if result.returncode != 0:
    goodhash = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()

    badhash = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

    print(f"Good hash (origin/main): {goodhash}")
    print(f"Bad hash (HEAD): {badhash}")

    os.system(f"git bisect start {badhash} {goodhash}")

    os.system("git bisect run python manage.py test")