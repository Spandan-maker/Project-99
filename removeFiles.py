import time
import os
import shutil

# Path and Seconds

path = str(input("Pls enter the name of the file/folder you want to delete: "))
days = time.time()

print("Collecting file/folder location...")
time.sleep(3)

# Checking if the path is correct and generating a code for the path's files and folders
checkPath = os.path.exists(path)

if checkPath == False:
    print("Oops!! Seems you have entered a path that doesn't exist")

pathList = os.walk(path)

# Folder creation time
ctime = os.stat(path).st_ctime

# Function to delete files
if ctime < 1650000000:
    if os.path.isdir(path):
        shutil.rmtree(path)
        
        print("Removing selected file/folder...")
        time.sleep(3)
        print("Removed " + path + " folder.")
    
    elif os.path.isfile(path):
        os.remove(path)

        print("Removing selected file/folder...")
        time.sleep(3)
        print("Removed " + path + " file.")

else:
    print("The file couldn't be deleted.")