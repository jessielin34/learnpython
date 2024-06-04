email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

#more accurate
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

import re

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")