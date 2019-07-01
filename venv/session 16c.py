import os

print(os.getcwd())
print(os.name)
#print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDir = "/Users/Rajeev yadav/Documents"
pathToFile = "/Users/Rajeev yadav/Documents/coonect may.pdf"
print("Is Downloads available:", os.path.exists(pathToDir))
print("Is connect may.csv available:", os.path.exists(pathToFile))

# path = "/Users/Rajeev yadav/Documents/MyPythonPrograms"
# os.mkdir(path)

# print(os.getcwd())
# os.chdir("/Users/Rajeev yadav/Documents/MyPythonPrograms")
# print(os.getcwd())
#
# print(os.getcwd())
#
# os.rmdir("/Users/Rajeev yadav/Documents/MyPythonPrograms")
# print(">> Directory Removed")

files = os.walk("/Users/Rajeev yadav/Documents")
print("files:",files)

allFiles = list(files)
for file in allFiles:
    print(file)

# Assignment
# Ask path of a folder from user as input
# Tell him how many number of audio files, video files and documents exists
# Explore : To find all those files which were created long ago and are not in use :)n