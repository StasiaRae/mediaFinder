import os, re, sys
fileExt = [".mp4",".jpg",".mp3"] #file extensions to search for
if (len(sys.argv) > 1):
    path = sys.argv[1] #checks if a path parameter was passed
else:
    path = os.getcwd() #uses current directory if no parameter was passed
    
def checkDirectory(file): #method to check whether a given file has the desired file extension
    for ext in fileExt:
            fileType = file[file.rfind("."): len(file)]
            if fileType.lower() == ext.lower():
                return True
dirSet = set("") #a set containing desired directories
i = 0
for root, dirs, files in os.walk(path): #loops through subdirectories
    for name in files: #loops through files
        file = os.path.join(root, name)
        if checkDirectory(file): #if a file matches the desired type, it is added to the set
            dirSet.add(root)
    i = i+1
    print "Checked " + '{:>10}'.format(str(i)) + " directories \r",
print ""
print "Generating file..."
dirList = list(dirSet) #set is converted to a list and sorted
dirList.sort()
out_file = open("media_directories.txt", "wb")
for dir in dirList:
    print dir
