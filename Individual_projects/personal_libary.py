#ES 1srt, personal libary

#make song a libary that is empty
song = []

#make a funtion called view and put songs inside of the parenthesis
def view(song):
    #if there is nothing on song print your library is empty 
    if not song:
        print("your library is empty.")
    #else for book in song and print with f strings
    else:
        for book in song:
            print(f"Your Library:\n {book}")
        
#make a funtion called add and put song inside of the parenthesis
def add(song):
    #make title be input title strip
    title = input("Title: ").strip()
    #make the arstist input, by 
    artist = input("By: ").strip()
    #make piece be title by artist 
    piece = (f"{title} by {artist}")
    #append piece to song
    song.append(piece)
    #print you have added 
    print(f"you have added {piece}")

#make a funtion called remove and put song inside of the parenthesis
def remove(song):
    #if song has no songs print that they have no songs print the is no books to remove and return
    if not song:
        print("\nthere are no books to remove.")
        return
    #print songs are for i in range(len(song))
    print("songs:")
    for i in range(len(song)):
        #print i +1 and song that has the number i 
        print(f"{i + 1}. {song[i]}")
    #make the choice that the user wants to delete, it has to be a number
    choice = input("Enter the number of the item you would like to remove: ").strip()
    #if the choice is digit make choice be an integer, by int(choice)
    if choice.isdigit():
        choice = int(choice)
        #if choice is less than one or less than the lenght of the song 
        if 1 <= choice <= len(song):
            #make remove equals song choice -1
            removed = song.pop(choice - 1)
            #print you have removed song
            print(f"You have removed {removed}")
        #else print please select an acual number
        else:
            print("please select an actual number")
    #else print plaase select an actual option
    else:
        print("please enter a valid number.")

#make a funtion called search and put song iside of th parenthesis
def search(song):
    #if there is no song print your libary is empty
    if not song:
            print("\nyour libary is empty.")
            return 
    #make a while true loop 
    while True:
        # make choice be enter the song name to search
        choice = input("\nenter the song name to search for: ").strip().lower()
        #make found equals false
        found = False
        # for s in songs, and if choice is in s and lower or .lower
        for s in song:
                if choice in s.lower():
                    #print s and make found True
                    print(s)
                    found = True
                    
        #if not found print song not found
        if not found:
                print("Song not found.")

        break
#define a funtion called menu
def menu():
    #make funtion = a tuple with the options the user can choose and putting numbers next to them
    options = ("1. View\n 2.Add\n 3.Remove\n 4.Search\n 5.Exit")
    #make a while loop
    while True:
        print(options)
        #options input what would you like to do?
        option =input("What would you like to do?").strip()
        #if option is 1
        if option =="1":
        #call view()
            view(song)
        #if optioin is 2
        elif option =="2":
        #call add()
            add(song)
        #if option is 3
        elif option=="3":
        #call remove()
            remove(song)
        #if option is 4
        elif option =="4":
        #call search
            search(song)
        #if option is 5 print thanks for using this
        elif option =="5":
            print("Exit selected")
            break
        #else print please slect another option
        else:
            print("pleas select another option that is avalible")
#call menu
menu()