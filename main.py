import subprocess
import sys
import os

file_path = "/Users/mohammedalnashrei/projects/MusicPlayer"
file_path = os.path.join(file_path, "command.py")
# print(file_path)
command = ["python3", file_path]
for i in range(1, len(sys.argv)):
    command.append(sys.argv[i])
    
subprocess.Popen(command)