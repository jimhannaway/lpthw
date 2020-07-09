# Printing out a nursery rhyme making use of these brackets{} and formatting
# to complete the rhyme.
print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")

# Inserting 10 dots in a line
print("." * 10) # what'd that do?

# Setting up the end variables to spell out Cheese burger when printed
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end. Try removing it to see what happens.
# ... of course the space gets removed but it also prints burger on a new line!
print (end1 + end2 + end3 + end4 + end5 + end6,end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
