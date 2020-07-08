# File seek
""" This shows file seek working.
    This example is fromhttps://code-maven.com/python-seek

    examples/python/seek.py """

import os

filename = 'dataseek.txt'
with open(filename, 'w') as fh:
    fh.write("Hello World!\nHow are you today?\nThank you!")

print(os.path.getsize(filename))  # 44

with open(filename) as fh:
    print(fh.tell())        # 0
    row = fh.readline()
    print(row)              # Hello World!
    print(fh.tell())        # 14

#    fh.seek(-7, os.SEEK_END) # Back seek disabled in python3.
    fh.seek(6, os.SEEK_SET)
    print(fh.tell())        # 6

    row = fh.readline()
    print(row)              # World!
    print(fh.tell())        # 14

    fh.seek(0, os.SEEK_SET)
    print(fh.tell())        # 0
    print(fh.read(5))       # Hello

    fh.seek(40, os.SEEK_SET)
    print(fh.tell())        # 40
    print(fh.read())        # you!
    print(fh.tell())        # 44
