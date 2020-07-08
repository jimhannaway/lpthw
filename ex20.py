# Functions & Files
# This shows functions and files working together to make useful stuff
# Import “argument vector,” the variable for any arguments
# passed to the program through the command line.

from sys import argv
# define the arguments being passed into the program: script and input_file
script, input_file = argv

# create function to print the while of the input_file
def print_all(f):
    print(f.read())

# create the function to rewind the file pointer to the first byte in input_file
def rewind(f):
    f.seek(0)

# create function to print specific file line referred to by line_count
def print_a_line(line_count, f):
    print(line_count, f.readline())

# set variable to open the input_file
current_file = open(input_file)

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
print(f"Current line is {current_line} which gets passed into print_a_line first arg(line_count).")

current_line += 1
print_a_line(current_line, current_file)
print(f"Current line is {current_line} which gets passed into print_a_line first arg(line_count).")

current_line += 1
print_a_line(current_line, current_file)
print(f"Current line is {current_line} which gets passed into print_a_line first arg(line_count).")