import os

# rename a file 
def renameFile(fileName):
    print("Old name: " + fileName)
    newName = input("New name: ")
    os.rename(fileName, newName)
    print("Done")

renameFile(input("Enter file name: "))