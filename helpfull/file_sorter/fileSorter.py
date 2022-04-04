import os, os.path, shutil, tkinter.filedialog

def getFileType(fileName):
    fileType = fileName[::-1]
    fileType = fileType[:fileType.index(".")]
    fileType = fileType[::-1]
    fileType = fileType
    return fileType.upper()

def sort(path):
    files_to_sort = os.listdir(path)

    ask = input("Put all folders to one folder?(y/n): ").lower()
    if ask == "y":
        if os.path.exists(path+"Folders") == False:
            os.mkdir(path+"Folders")
            for i in files_to_sort:
                if os.path.isdir(path+i):
                    shutil.move(path+i,path+"Folders")
        else:
            if os.path.isdir(path+i):
                    shutil.move(path+i,path+"Folders")
    
    for i in files_to_sort:
        if os.path.isfile(path+i):
            fileType = getFileType(i)
            if not os.path.exists(path+fileType):
                os.mkdir(path+fileType)
            
            shutil.move(path+i,path+fileType)

print("1. On Desktop\n2. Chose path")
answer = int(input("Where sort?: "))
os.system('cls')
if answer == 1:
    pathToSort = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/"
elif answer == 2:
    pathToSort = tkinter.filedialog.askdirectory()+"/"
    print(pathToSort)

sort(pathToSort)