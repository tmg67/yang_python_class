import subprocess
import os

#run a simple command and capture its output
result = subprocess.run(["echo", "hello world"], capture_output=True, text=True)
print("command output:", result.stdout)

#list files in the  current directory using `ls` or `dir` (platform-n specific)
command = ["ls"] if os.name != "nt" else ["dir"]
result = subprocess.run(command, capture_output=True, text=True)
print("files in current directory")
print(result.stdout)

#check for errors (e.g., invalid command)
result = subprocess.run(["fake_command"], capture_output=True, text=True)
if result.returncoodee != 0:
    print("error:", result.stderr)