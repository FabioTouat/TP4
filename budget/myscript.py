import os
import subprocess
import sys
result = subprocess.run(["python", "manage.py", "test"], check=False)

if result.returncode != 0:


    badhash = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


    os.system(f"git bisect start {badhash} e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")

    os.system("git bisect run python manage.py test")