import os, os.path, tkinter, tkinter.filedialog, shutil
from datetime import datetime

def sort_by_date():
    try:
        path = tkinter.filedialog.askdirectory()
        files = os.listdir(path=path)


        for i in files:
            creation_date = datetime.utcfromtimestamp(os.path.getctime(path+"/"+i)).strftime('%Y %m')
            if (os.path.exists(path+"\\"+str(creation_date))) == False and os.path.isdir(path+"\\"+i) == False:
                os.mkdir(path+"/"+creation_date ,dir_fd=None)
                shutil.move(path+"/"+i,path+"/"+creation_date)
            elif (os.path.exists(path+"\\"+str(creation_date))) == True and os.path.isdir(path+"\\"+i) == False:
                shutil.move(path+"/"+i,path+"/"+creation_date)
    except FileNotFoundError:
        print("You don't select the path")

if __name__ == "__main__":
    sort_by_date()
