import os
import subprocess
import sys


command = "python3 main.py"
for i in range(1, len(sys.argv)):  
    command += " " + sys.argv[i]
subprocess.Popen(command.split())
# os.system(command + " &")
# print(command)
# print(sys.argv)

# subprocess.Popen("python test.py", shell=True)