#ES 1rst morse code translator

#make a tuple for the english alphabet and the morse code in alphabilical order 
english = (
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',' '
)
morse = (
    '.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
    '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
    '..-','...-','.--','-..-','-.--','--..',' '
)

#make a funtion for morse to english
def morse_to_english():
    # mkae a loop for in in range 
    for i in range(len(english)):
        #then print english match the morse
        print(f"{english[i]} : {morse[i]}")
    #make a while loop and make user equals input what they want the sequence
    while True:
        user = input("Please select the pattern to translate (use spaces between letters, double space between words):\n")
        #make symbols equals user split 
        symbols = user.split(" ")
        #make an empty list 
        result = [] 
        #make invalid be false
        invalid_input = False
        #make skip next false 
        skip_next = False 
        #make i symbol in enumerate symbols
        for i, symbol in enumerate(symbols):
            #detect double spaced words, and append space to the list
            if symbol == "" and not skip_next:
                result.append(" ") 
                skip_next = True
                continue
            #if symbol is not in morse print to select an acutal answer, make invalid true and break
            skip_next = False
            if symbol not in morse:
                print("Please select a valid option")
                invalid_input = True
                break
            #make posiotion equals morse index trying to find the symbol 
            position = morse.index(symbol)
            #make the letter equals the possion in english
            letter = english[position]
            #append the letter to results
            result.append(letter)
        # if invalid is true print to try agian and continue to go back to the loop 
        if invalid_input == True:
            print("Try again.\n")
            continue
        #make final messege equals a empty string
        final_message = ""
        #make a loop that adds the letters to the list 
        for char in result:
            final_message += char 
        #print the final messege 
        print("\nYour message says:")
        print(final_message)
        break 

            
#make a funtion from english to morse
def english_to_morse():
    #make a while loop and ask the user what letters they want to use 
    while True:
        user = input("Please type the message in English to translate to Morse:\n").lower()
        #make an empty library 
        result = []
        #and make invalid input false 
        invalid_input = False
        #make and loop and inside make sure the input is a letter 
        for char in user:
            if char not in english:
                print("Please select a letter ")
                invalid_input = True
                break
            #make position equals english index 
            position = english.index(char)
            #make the morse code in letters then append it to the list
            morse_char = morse[position]
            result.append(morse_char)
        #if invalid is true print to try agian and continue to go back to the loop 
        if invalid_input:
            print("Try again.\n")
            continue

        # print the final message 
        final_message = " ".join(result)
        print("\nYour message in Morse code is:")
        print(final_message)
        break

#make a funtion for main menu
def main():
    #make a while loop
    while True:
        #make the user input the option of where they want to go, name it choice
        choice = input("\n\n1:Morse to english\n2:English to morse\n3:Exit\n").strip()
        #if choice is 1. call morse_to_english
        if choice == "1":
            morse_to_english()
        #if choice is 2. call english to morse
        elif choice == "2":
            english_to_morse()

        #if choice is 3. print that they have decided to leave, break
        elif choice == "3":
            print("You have dicided to exit")
            break 
        #else print to select an acutal option, continue
        else:
            print("Please select an acutal option listed")
main()