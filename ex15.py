# Reading files
# Changed directory in lpthw directory which simplifies the run script command to
# python ex15.py ex15_sample.txt

# import the arguments variable
from sys import argv

# set the script and filename arguments
script, filename = argv
# set variable txt to open the filename passed in as an argument
txt = open(filename)
# print the message stating the filename and print the text held in the file
print(f"Here's your file {filename}:")
print(txt.read())
# print a message prompting with an > char for re-entry of the filename
print("Type the filename again:")
file_again = input("> ")
# set the txt_again variable to open the new variable holding the new filename
txt_again = open(file_again)
# print the text held in the file
print(txt_again.read())
# close files before ending script
txt.close()
txt_again.close()
### txt_again= close(file_again)
print(f"Thats both {txt_again} and {txt} filename variables now closed.")
