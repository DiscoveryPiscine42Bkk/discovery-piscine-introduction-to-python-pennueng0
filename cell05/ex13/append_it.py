import sys
import re 

args = sys.args[1:]

if not args:
    print("none")
else:
    for word in args:
        if not re.search(r'ism$', word):
            print(f"{word}ism")