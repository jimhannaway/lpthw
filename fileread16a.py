# Reading and writing files
# Part2. This script reads the file created in ex16. WORKS OK.
# Part2 is run manually/separtely after script 16 has set up test.txt file.

# import the arguments variable
from sys import argv

# set the script and filename arguments
script, filename = argv

target_read = open(filename)
print(target_read.read())

target_read.close

#Part3 acts as a function to be called from ex16. NOT WORKING
# def read(filename)
#    return target = open(filename)
#    print(target.read())
