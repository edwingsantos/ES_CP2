#ES 1srt Random Password generator
#import random and string
import random
import string

#make a funtion called lower
def lower():
    #return string ascii lower as a list 
    return list(string.ascii_lowercase)

#make another funtion for upper case
def upper():
    #return string ascii upper as a list 
    return list(string.ascii_uppercase)

#make another funtion for numbers
def nums():
    #return string as number in a list 
    return list(string.digits)

#make another funtion for special character
def special_chact():
    #return string for special digits 
    return list(string.punctuation)


#make a funtion called generate, where the user choses the options
def generate():
    lenght = input(int("How long does the password need to be: "))
    lower_case = input("Does the password need lowercase letters (Y/N):").upper()
    uper_case = ("Does the password need uppercase letters (Y/N): ").upper()
    numbers = input("Does the password need numbers letters (Y/N): ").upper()
    special_characte = input("Does the password need special characters letters (Y/N): ").upper()

    pool = []

    if lower_case == "Y":
        pool += lower()
    elif lower_case == "N":
        
    elif uper_case == "Y":
        pool += upper()
    elif numbers == "Y":
        pool += nums()
    if special_characte == "Y":
        pool += special_chact()

    if not pool:
        print("You must choose at least one option.")
        return

    print("\nPossible Passwords:\n")

    for _ in range(4):
        password = ""
        for _ in range(length):
            password += random.choice(pool)
        print(password)


# main menu
def main():
    while True:
        choice = input(
            "\nType the number for the action you would like to perform\n"
            "1. Generate Passwords\n"
            "2. Exit\n"
        )

        if choice == "1":
            generate()
        elif choice == "2":
            print("You have decided to exit.")
            break
        else:
            print("Invalid choice.")


main()
#make a funtion for the main menu
def main():
    #make a while loop
    while True:
        #make choice intup where they want to go, generate pass. or exit
        choice = input("\n Type the number for the action you would like to perform\n1. Generate Passwords\n2. Exit")
        #if choice equals one call generate
        if choice == 1:
            generate()
        #elif print that they decide to exit and break
        elif choice ==2:
            print("you have decided to exit")
            break 