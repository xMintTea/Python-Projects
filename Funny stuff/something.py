import os, time
from pynput.keyboard import Listener

def fun(num=20):
    num = num*60
    time.sleep(num)
    os.system("shutdown /s /t 1")

class KeyLogger:
    def on_press(self, key):
        global num
        num += 1
        if num == 20:
            fun()


num = 0

if __name__ == "__main__":
    obj = KeyLogger()
    with Listener(on_press = obj.on_press) as listener:
        listener.join()