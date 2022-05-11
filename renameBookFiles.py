import os

# rename all files with the pdf extension 
def renameFiles(dirName):
    # get all files in the directory
    fileList = os.listdir(dirName)
    print(fileList)
    for fileName in fileList:
        if fileName.endswith(".epub"):
            if (fileName[0:1] == " "):
                print(fileName[1:])
                fileName2 = fileName[1:]
                os.rename(dirName + "/" + fileName, dirName + "/" + fileName2)
    print("Done")
    
renameFiles("/Users/omarm/Media/Books")



# start = fileName.find("[");
# end = fileName.find("]")
# if ((start != -1) and (end != -1)):
#     author = fileName[(start+1):end]
#     newName = fileName.replace("[" + author + "]", "")
#     index = newName.find(".pdf")
#     fileName2 = newName[:index] + ' [' + author + ']' + newName[index:]
#     print(fileName2)
# else:
#     fileName2 = fileName