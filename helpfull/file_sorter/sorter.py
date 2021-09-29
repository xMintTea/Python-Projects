import tkinter, os, shutil, tkinter.filedialog, tkinter.messagebox

def file_type_da(file_name):
    if "." not in file_name:
        pass
    else:
        file_type = file_name[::-1]
        dote = file_type.index('.')
        file_type = file_type[:dote]
        file_type = file_type[::-1]
        if " " in file_type:
            index = file_type.index(" ")
            file_type = file_type[:index]
        return file_type


username = os.environ.get( "USERNAME" )
sort_folder = "C:\\Users\\{}\\Desktop\\sort".format(username)
sort_files_in_folders = sort_folder+"\\"+"files_in_folders_sort"

if os.path.exists(sort_folder) == True:
    if os.path.exists(sort_files_in_folders) == True:
        pass
    else:
        os.mkdir(sort_files_in_folders)
else:
    os.mkdir(sort_folder, dir_fd=None)


files = (os.listdir(path=sort_folder))

for i in files:
    try:
        file_type = file_type_da(i)
    except ValueError:
        continue
    try:
        NewPath = sort_folder+"\\"+file_type.upper()
    
        if os.path.exists(NewPath) == False:
            os.mkdir(NewPath, dir_fd=None)

        kk = file_type in i

        if kk == True:
            shutil.move(sort_folder+"\\"+i,NewPath)
        else:
            continue

        for ii in files:
            isFile = os.path.isdir(sort_folder+"\\"+ii)

            if isFile == True:
                if len(os.listdir(sort_folder+"\\"+ii)) == 0 and not sort_files_in_folders:
                    os.rmdir(sort_folder+"\\"+ii, dir_fd=None)
    except:
        continue



for i in files:
    try:
        check_empty_folder = (os.listdir(path=sort_folder+"\\"+i))
        if os.path.isdir(sort_folder+"\\"+i) == True and len(check_empty_folder) == 0:
            os.rmdir(sort_folder+"\\"+i, dir_fd=None)
    except NotADirectoryError:
        if os.path.exists == False:
            os.mkdir(sort_folder+"\\"+"FILES")
            shutil.move(sort_folder+"\\"+i,sort_folder+"\\"+"FILES")
        else:
            shutil.move(sort_folder+"\\"+i,sort_folder+"\\"+"FILES")
        

