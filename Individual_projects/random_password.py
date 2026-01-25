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
    input("what would you like to do")


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