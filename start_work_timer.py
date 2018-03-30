# screen -dmS work_timer python path/start_work_timer.py
import time
import subprocess

time.sleep(1)
subprocess.call("/usr/bin/pmset displaysleepnow", shell=True)
