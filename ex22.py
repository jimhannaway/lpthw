# File aggregation
""" This script reads through the lpthw directory
    and appends each script to a new file """

import os
import sys
import glob


# Set path to the current directory and print it out.
path = os.getcwd()
print(f"Current directory is: {path}")

# Get all the files in that directory and print a sample of their names
files = os.listdir(path)
print("Files in '%s': %s" % (path, files))
print(files[0], files[3], files[5])

##pyfiles = []
##for file in glob.glob("*.py"):
##    pyfiles.append(file)
##print(f"This is pyfiles list: {pyfiles}")

mylist = [f for f in glob.glob("*.py")]
#remove the last item in the list
# mylist.pop() ## no longer required

# remove ex20.py which requires a filename input as an argv parameter
del mylist[14]
print(f"This is the list called mylist: {mylist}")

#walk through all files in current directory
#path = 'C:\Users\Jim\Documents\Python Scripts\lpthw'

print("OPENING AGGREGATE FILE.")
fh = open('PythonAggregates1.txt', 'a')

for filename in mylist:
    try:
        fR = open(filename, "r")
        print(f"Opening: {filename}")
    except IOError:
        print("Could not open File: " + filename)
        sys.exit()

    try:
        fh.write("\n*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        fh.write(filename.upper())
        fh.write("\n*-*-*-*-*-*-*-*-*-*-*-*-*\n\n")
        for x in fR.readlines():
            fh.write(x)
    except IOError:
        print("Could not write file: " + filename)
        sys.exit()


    fR.close()
    print("close fileRead")
fh.close()
print("close fileWrite")
