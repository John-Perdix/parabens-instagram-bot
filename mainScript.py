import subprocess
import time

# List of scripts to run in order
scripts = ["instagram-bot.py", "faceDetection.py", "post-stories.py"]

while True:
    for script in scripts:
        result = subprocess.run(["python", script], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully ran {script}")
            print(result.stdout)
        else:
            print(f"Error running {script}")
            print(result.stderr)
    
    # Add a delay (optional)
    time.sleep(60)  # Adjust the delay time as needed