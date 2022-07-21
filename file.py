import subprocess
import sys


command = "python3 main.py"
for i in range(1, len(sys.argv)):  
    command += " " + sys.argv[i]
subprocess.run(command.split(), capture_output=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
