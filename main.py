from generator import generator as g
from insultor import insultor as i

if __name__ == "__main__":
    initialText = """ Hello :D
    Please select an option:
    1) Password Generator
    2) Password Rater
    3) Quit Program
    """
    userInput = int(input(initialText))

    match userInput:
        case 1:
            file_path = "text_files/passwords.txt"
            print(g(file_path))
        case 2:
            userInput1 = input("What's your password?\n")
            #Possible addition, every character put in input be turned into an *
            print(i(userInput1))
        case 3:
            exit()
        case _:
            print("Invalid Input!")
