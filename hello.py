#Ask user for their name
name = input("What's your name?: ")

#Split user's name into first name and last name
first, last = name.split(" ")

#Remove whitespace from str
name = name.strip()

#Remove whitespace from str and capitalize user's name
#name = name.strip().title()

#capitalize user's name
name = name.title()

#say hello to user
print(f"hello, {name}")

#create a function
def hello(to="world"):
    print("hello,", to)