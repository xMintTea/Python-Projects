import os,shutil
username = os.environ.get( "USERNAME" )

path = "C:\\Users\\{}\\Desktop\\sort".format(username)


if os.path.exists(path) == True:
    pass
else:
    os.mkdir(path, dir_fd=None)



files = (os.listdir(path=path))

if len(files) == 0:
    print("Please add the files to the folder")
else:
    for i in files:
        try:
            dote = i.index(".")
        except ValueError:
            continue

        file_type = (i[dote:])
        
        NewPath = path+"\\"+i[dote+1:].upper()


        if os.path.exists(NewPath) == False:
            os.mkdir(NewPath, dir_fd=None)
        else:
            pass
        
        kk = file_type in i[0:]

        if kk == True:
            shutil.move(path+"\\"+i,NewPath)
        else:
            continue
            

