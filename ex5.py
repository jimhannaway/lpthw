name = 'Jimmy Hannaway'
age = 55 #not a lie
height = 68 #inches
weight = 196 #lbs
eyes = 'blue'
teeth = 'white-ish'
hair = 'brown'
cm = height * 2.54
kg = weight / 2.2046

print (f"Let's talk about {name}.")
print (f"He's {age} years old and {height} inches tall.")
print (f"He's {weight} pounds heavy.")
print (f"So in metric he is {cm:.1f}cm tall and {kg:.1f}kg heavy." )
print ("Actually that's a bit overweight!")
print (f"He's got {eyes} eye and {hair} hair.")
print (f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky so try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height} and {weight} I get {total}.")
