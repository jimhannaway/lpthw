# Names, Variables, Code, Functions
# Functions do 3 things, they
    # name pieces of Code the way variables name strings and numbers
    # take arguments the way scripts take argv
    # let you make your own "mini commands" using these first 2 things

# this function is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok that args is actually pointless, we can do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Jim", "Hannaway")
print_two_again("James", "Hannaway")
print_one("FirstArg")
print_none()