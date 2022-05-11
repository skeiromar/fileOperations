# delete files ending with the extension .pdf
import os


def deleteFiles(dirName):
    # get all files in the directory
    fileList = os.listdir(dirName)
    print(fileList)
    for fileName in fileList:
        if fileName.endswith(".ithmb"):
            os.remove(dirName + "/" + fileName)

deleteFiles("/Users/omarm/Media/Pictures1")