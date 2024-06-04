url = input("URL: ").strip()
print(url)

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

import re
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")