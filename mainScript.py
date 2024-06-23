import subprocess

# List of scripts to run in order
scripts = ["instagram-bot.py", "script2.py", "script3.py"]

for script in scripts:
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully ran {script}")
        print(result.stdout)
    else:
        print(f"Error running {script}")
        print(result.stderr)