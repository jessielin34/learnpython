for _ in range(3):
    print("#")

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

    #print("#\n" * height, end="")
        
def main():
    print_row(4)
    print_square(3)

def print_row(width):
    print("#" * width)

def print_square(size):
    #for each row  in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        #print new line for each row
        print()

main()