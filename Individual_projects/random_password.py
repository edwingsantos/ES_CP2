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

#make a funtion for check 
def check(choice):
    #make a while loop, make answer equals input what the user says 
    while True:
        answer = input(choice).strip().upper()
        #if the answer is yes return true
        if answer == "Y":
            return True
        #if the answer equals no return false
        elif answer == "N":
            return False
        #else print to select an actuel option
        else:
            print("please select an actuel option")

#make a funtion called generate 
def generate():
    #Make a while loop
    while True:
        #make lenght equal an integer input, asking how long the password is going to be
        length = input("How long does the password need to be: ")
        #if lenght is digit, break else print to select a number
        if length.isdigit():
            length = int(length)  # convert to integer for later use
            break
        else:
            print("Select another option that is a number")
            continue

    #make the different options to choose equals check with the quiestion 
    lower_case = check("Does the password need lowercase letters (Y/N): ")
    upper_case = check("Does the password need uppercase letters (Y/N): ")
    numbers = check("Does the password need numbers (Y/N): ")
    special_character = check("Does the password need special characters (Y/N): ")
    
    #make a empty library called requirements
    requirements = []
    #if the quiestion equals yes, add it to requiremnets according to the quiestion
    if lower_case:
        requirements += lower()
    if upper_case:
        requirements += upper()
    if numbers:
        requirements += nums()
    if special_character:
        requirements += special_chact()
    #if there is nothing is requirements print that you have to put things to create, then return
    if not requirements:
        print("you must have a requirement")
        return 

    print("\nPossible Passwords:")
    #make a loop 4 times, for i in range
    for i in range(4):
        #make password empty and do another loop, but now in range lenght
        password = ""
        for i in range(length):
            #make password add random choice from requrements. Then print the password
            password += random.choice(requirements)
        print(password)
#make the funtion for the main meny
def main():
    #make a while loop and make choice input what they want to do
    while True:
        choice = input("\nType the number for the action you would like to perform\n""1. Generate Passwords\n""2. Exit\n")
        #if the choice is 1, call generate
        if choice == "1":
            generate()
        #elif choice is 2 pritn that you have decided to exit, break
        elif choice == "2":
            print("You have decided to exit.")
            break
        #else print to put something taht is 
        else:
            print("choose 1 or 2")
#call main
main()
