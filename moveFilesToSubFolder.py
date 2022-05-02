#!/usr/bin/env python3
# Path: moveFilesToSubFolder.py

# move all files with certain type and name to a subfolder
import os

def createDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " + dirName + " created")
    else:
        print("Directory " + dirName + " already exists")

def moveFilesToSubFolder(dirName):
    # get all files in the directory
    fileList = os.listdir(dirName)
    print(fileList)
    for fileName in fileList:
        if fileName.endswith(".png") and fileName.__contains__("Screen Shot"):
            createDir(dirName + "/screenshots")
            os.rename(dirName + "/" + fileName, dirName + "/" + "screenshots" + "/" + fileName)
    print("Done")

moveFilesToSubFolder(input("Enter directory name: "))
