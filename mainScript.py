import subprocess
import time
import datetime

# List of scripts to run in order
scripts = ["instagram-bot.py", "gemini.py", "faceDetection.py", "post.py"]

# Function to log output to a file
def log_output(script_name, output):
    with open(f"logs/{script_name}_log.txt", "a") as log_file:
        log_file.write(f"=== Execution at {datetime.datetime.now()} ===\n")
        log_file.write(output)
        log_file.write("\n\n")

while True:
    for script in scripts:
        try:
            result = subprocess.run(["python", script], capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                print(f"Successfully ran {script}")
                log_output(script, result.stdout)
            else:
                print(f"Error running {script}")
                log_output(script, result.stderr)
        except subprocess.TimeoutExpired:
            print(f"Timeout expired while running {script}")
            log_output(script, "Timeout expired\n")
        except Exception as e:
            print(f"Exception occurred while running {script}: {str(e)}")
            log_output(script, f"Exception occurred: {str(e)}\n")
    
    # Add a delay
    time.sleep(60)
