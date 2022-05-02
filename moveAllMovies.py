
import os 

def moveAllMovies(dirName):
    # check the subfolder for any files ending with .mp4 or .mkv
    # if found, move them to another folder

    # get all files in the directory
    fileList = os.listdir(dirName)
    for fileName in fileList:
        if os.path.isdir(dirName + "/" + fileName):
            subFileList = os.listdir(dirName + "/" + fileName)
            for subFileName in subFileList:
                if (subFileName.endswith(".mp4") or subFileName.endswith(".mkv")) and not fileName.__contains__("Video"):
                    os.rename(dirName + "/" + fileName, "/Users/omarm/media/Movies/" + fileName)
                    print("Moved " + fileName + " to /Users/omarm/media/Movies")


moveAllMovies("/Users/omarm/Downloads")