import os
from random import randint


def folder(da):
    # Create 1000 folders in Ur desktop
    username = os.environ.get( "USERNAME" )
    path = f"C:/Users/{username}/Desktop"
    
    for i in range(da):
        num = randint(1,99999)
        os.mkdir(path+"/"+str(num))
if __name__ == "__main__":
    folder(1000)
