# Prompting and passing

from sys import argv

script, username, surname = argv
prompt = '***> '

print(f"Hi {username} {surname}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {username}?")
likes = input(prompt)

print(f"Where do you live {username}?")
lives = input(prompt)

print(f"{username}, what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, {username} {surname} so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
