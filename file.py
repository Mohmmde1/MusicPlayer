import subprocess
import sys


command = ["python3", "main.py"]
for i in range(1, len(sys.argv)):
    command.append(sys.argv[i])
    
subprocess.Popen(command)