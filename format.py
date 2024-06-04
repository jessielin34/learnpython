name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"hello, {name}")

import re

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
    #name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")