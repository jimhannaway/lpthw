# Some escape sequences.
# Useful for chars in difficult to type variables

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(fat_cat2)

# Using more escape sequences
# \'Single-quote (')
# \" Double-quote (")
singlequotes = "\'\'\'"
print(singlequotes)
print("\"Some uses for escape sequences.\"")
print(singlequotes)
print ("\\") #prints a single backslash

# \a ASCII bell (BEL)
print("\a Hear that?") # Sounds the Microsoft soft bell.

# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII newline (LF)
# \r Carriage return (CR)
# \t Horizntal tab (TAB)

print("Now...\nthats a line feed")
print("Now...thats a ba\bckspace feed taking out the a char")
print("Now...this is what a form feed char looks like on-screen\f")
print("Now...this is what a carriage return looks like on-screen\r")
print("Now...this is what\thappens when\tyou tab in a string!")

# \N{name] Character name in the Unicode database (Unicode only)
# \uxxxx   Character with a 16-bit hex value xxxx
# \uxxxxxxxx    Character with a 32-bit hex value xxxx
# \xhh     Character with hex value hh
# \000     Character with octal value 000
# \v       ASCII vertical tab (VT)
print("\N{hyphen} it's a hyphen")
print("\u0096 cant find a 16-bit hex value!")
print("\u00000115 cant find a 32-bit hex value!")
print("\x6E lower-case N") # hex value for lower case n
print("\067 it's a seven") # octal value for 7
print("\v shold be vertical tab now!") # vertical tab

print("Not covered in glory here.\n\nNot sure I am getting a good understanding!")
