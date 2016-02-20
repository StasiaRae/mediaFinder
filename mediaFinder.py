import os, re, sys
fileExt = [".mp4",".jpg",".mp3"] #file extensions to search for
if (sys.argv[1]):
    path = sys.argv[1] #checks if a path parameter was passed
else:
    path = os.getcwd() #uses current directory if no parameter was passed
for root, dirs, files in os.walk(path): #loops through all files and subdirectories
    for name in files:
        file = os.path.join(root, name)
        for ext in fileExt:
            fileType = file[file.rfind("."): len(file)] #extracts the file extension from the file path
            if (fileType.lower() == ext.lower()): #checks if file matches a desired type
                print file
