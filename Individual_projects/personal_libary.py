#ES 1srt, personal libary

#make song a libary that is empty
song = []

#make a funtion called view and put songs inside of the parenthesis
def view(song):
    print("h")

#make a funtion called add and put song inside of the parenthesis
def add(song):
    print("h")

#make a funtion called remove and put song inside of the parenthesis
def remove(song):
    #if song has no songs print that they have no songs, and call menu
    if not song:
        print("There are no songs, plase add some songs")




#make a funtion called search and put song iside of th parenthesis
def search(song):
    print("h")




#define a funtion called menu
def menu():
    #make funtion = a tuple with the options the user can choose and putting numbers next to them
    options = ("1. View\n 2.Add\n 3.Remove\n 4.Search\n 5.Exit")
    #make a while loop
    while True:
        #if option is 1
        if options ==1:
        #call view()
            view()
        #if optioin is 2
        elif options ==2:
        #call add()
            add()
        #if option is 3
        elif options==3:
        #call remove()
            remove()
        #if option is 4
        elif options ==4:
        #call search
            search()
        #if option is 5 print thanks for using this
        elif options ==5:
            print("thanks for using this thing my teacher made me do ")
        else:
            print("pleae select another option that is avalible")
menu()