import os

def moveFolder(src, dest):
    # get all files in the directory
    fileList = os.listdir(src)
    print(fileList)
    for fileName in fileList:
        os.rename(src + "/" + fileName, dest + "/" + fileName)
    print("Done")

moveFolder(input("Enter source directory name: "), input("Enter destination directory name: "))