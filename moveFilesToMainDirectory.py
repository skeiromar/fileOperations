# move files within subfolders into the main folder within a directory 
import os


def moveFiles(dirName):
    # get all files in the directory
    fileList = os.listdir(dirName)
    print(fileList)
    for fileName in fileList:
        if os.path.isdir(dirName + "/" + fileName):
            moveFiles(dirName + "/" + fileName)
        else:
            # move files to the main directory
            os.rename(dirName + "/" + fileName, "/Users/omarm/Media/Pictures1" + "/" + fileName)
    print("Done")


moveFiles("/Users/omarm/Media/Pictures1")