# Reading and writing files
# Commands to remember:
# close: Closes the file, like File > Save... in your editor.
# read: Reads the contents of the file. You can assign the result to a variable.
# readline: Reads jus one line of a text file.
# truncate: Empties the fie. Wach out if you care about the file.
# write('stuff'): Writes "stuff" to the file.
# seek(0): Moves the read/write location to the begnning of the file.

# import the arguments variable and the file read module 16a
from sys import argv
# import fileread16a ### removed NOT WORKING, see related comments below

# set the script and filename arguments
script, filename = argv

# Initial program user info and directions.
print(f"We are going to erase {filename}.")
print(f"If you don't want that hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

# Awaits user decision, dislays a ? while waiting.
input("?")

# If the user has selected CTRL+C the program will end, otherwise it continues from here.
# A user message is followed by setting the variable "target" to
# open the filename supplied in the argv parameter for writing
print("Opening the file...")
target = open(filename, 'w')
# User message that prevous filecontents will be erased (by .truncate)
print("Truncating the file. GOODBYE OLD TEXT!")
target.truncate()

# Program now requests three lins of text for writing to the file.
print("Now I will ask for three lines of text.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# Write the three lines provided by the user into the file
print("I am going to write these lines to the file.")
# Reaplce six target.write commands with a single line.
## target.write(line1)
## target.write("\n")
## target.write(line2)
## target.write("\n")
## target.write(line3)
## target.write("\n")
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
# and an alternative method which puts each line within quotes
## target.write('%r\n%r\n%r\n' % (line1, line2, line3))

#Now read the file using module 16a. NOT WORKING. Call fileread.py manually
## fileread16a.read(target)

# self explanatory...close the file
# important to .close as this sets the proper file attributes.
print("And finally, we close the file.")
target.close
