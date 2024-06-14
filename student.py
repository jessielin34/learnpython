class Student: 
    def __init__(self, name, house):
        self.name = name
        self.house = house
def main():
    name = get_name()
    house = get_house()
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
