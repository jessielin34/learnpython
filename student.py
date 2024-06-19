class Student: 
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name") 
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse"
            case "Otter":
                return "Otter"
            case _:
                return "/"

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
    student = Student(name, house) 
    return (name, house)
    #try:
        #return Student(name,house)
    #except Value:

if __name__ == "__main__":
    main()
