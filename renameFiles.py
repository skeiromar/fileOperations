import os

def renameFiles(dirName):
    # get all files in the directory
    fileList = os.listdir(dirName)
    print(fileList)
    for fileName in fileList:
        os.rename(dirName + "/" + fileName, dirName + "/" + fileName.replace(" ", "_"))
    print("Done")


isValidInput = False

while not isValidInput:
    dirName = input("Enter directory name: ")
    if os.path.isdir(dirName):
        isValidInput = True
        renameFiles(dirName)
    else:
        print("Not a valid directory name")