# import subprocess
# import sys


# command = "python3 main.py"
# for i in range(1, len(sys.argv)):  
#     command += " " + sys.argv[i]
# subprocess.run(command.split(), capture_output=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


import multiprocessing
import os
import psutil


def get_pids_by_script_name(script_name):

    pids = []
    for proc in psutil.process_iter():

        try:
            cmdline = proc.cmdline()
            pid = proc.pid
        except psutil.NoSuchProcess:
            continue
        # print(cmdline, "\n")
        # print(proc)
        # and os.path.basename(cmdline[1]) == script_name
        # if (len(cmdline) >= 2
        #     and 'main.py' == cmdline[1]):
        #     # print(cmdline)
        #     # print(proc)
        #     # proc.kill()
        #     pids.append(pid)
        # if  proc.name == "Python":
        #     print(proc)
        # print(proc.name())
        if proc.pid == 14029:
            # print(proc.pid==13215)
            for child in proc.children():
                print(child)
                child.kill()
            # print(proc)
        

    return pids


print(get_pids_by_script_name('main.py'))

for p in multiprocessing.active_children():
    print(p)
