# More Files: Reading and writing files
# Commands to remember:
    # close: Closes the file, like File > Save... in your editor.
    # read: Reads the contents of the file. You can assign the result to a variable.
    # readline: Reads just one line of a text file.
    # truncate: Empties the file. Wach out if you care about the file.
    # write('stuff'): Writes "stuff" to the file.
    # seek(0): Moves the read/write location to the begnning of the file.

# import the arguments variable and the file read module 16a
from sys import argv
from os.path import exists # reurns TRUE if a file exists

# set the script and filename arguments
script, from_file, to_file = argv

# we could do these next two lines in one line, how?
in_file = open(from_file)
indata = in_file.read()

# Initial program user info and directions.
print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
###print("Ready, hit ENTER to continue, CTRL-C to abort.") ### this line moved to the input statement.

# Awaits user decision, displays nothing () or whatever is in the brackets (Reay, hit ...).
###input()
input("Ready, hit ENTER to continue, CTRL-C to abort.")

# open out_file for writing indata to it
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# self explanatory...close both files
# important to .close as this sets the proper file attributes.
in_file.close()
out_file.close()
