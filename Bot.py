import os
import time
os.system("cd require && pip install -r requirements.txt")
os.system("cd require && pip3 install -r requirements.txt")
os.system("clear")
print("\033[1;32;40mWait Untill The Entire Program Get Finished.\033[1;31;40mOtherwise...")
time.sleep(5)
os.system("cd core && python lol.py")

