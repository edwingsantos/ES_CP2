#ES 1rst updated personal library
#import csv
import csv
#make a string be the relative path to your csv file
file_path = "Individual_projects/library.csv"
#make the order of the csv files be a tuple so it doenst change
field = ("title", "creator", "year", "genre")

#make a funtion for load  
def load():
    #make an empty library
    library = []
    #open the file and read it as file 
    try:
        with open(file_path,"r", newline="") as file:
            #read the file from line to line 
            reader = csv.DictReader(file)
            library = list(reader)
    #make a except thing that if the line is not found on the file then creates a file outomatically 
    except FileNotFoundError:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()
    #return the list 
    return library

#make a funtion for safe
def save(library):
    #open the file path and write it with a new line as file 
    with open(file_path, "w", newline="") as file:
        #make filednames a tuple of the info 
        fieldnames = ("title", "creator", "year", "genre")
        #make a string read the file line by lane and safe it
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(library)
    #print that the libary is safed
    print("library saved\n")

#make a funtion for check 
def check(library):
    #if liabry is empty print that is empty and return 
    if not library:
        print("library is empty\n")
        return
    #then make a loop and enumerate the libary starting at one, then for every item it adds one more
    for i, item in enumerate(library, 1):
        print(f"{i}. {item['title']} by {item['creator']}\n")

#make a funtion to show
def show(library):
    #if the library is empty the print the library is empty and return
    if not library:
        print("library is empty\n")
        return
    #make a loop and enumarate the libary starting with one 
    for i, item in enumerate(library, 1):
        #print the item is i 
        print(f"\nitem {i}")
        #make another loop and make value in item
        for key, value in item.items():
            #print the key equals the value
            print(f"{key}: {value}\n")

#make a funtion for add 
def add(library):
    #make strings asking the user for the title, creator, year, and genre. And name them according to their category
    title = input("Title: ").strip()
    creator = input("Creator: ").strip()
    year = input("Year: ").strip()
    genre = input("Genre: ").strip()
    #make item be a dictionary and put the item and the string as a value according to the category
    item = {"title": title, "creator": creator, "year": year, "genre": genre,}
    #append to library the item and print that the item is added
    library.append(item)
    print("item added\n")

#make a funtion for delete
def delete(library):
    #call check so the user knows what things there are
    check(library)
    #make choice be a input asking what number they want to delete
    choice = input("What number you want to delete: ").strip()
    #if the choice is not digint print to select an actual number and return 
    if not choice.isdigit():
        print("Please enter a valid number\n")
        return
    #make place equals a choice minus one 
    place = int(choice) - 1
    #check that place is grater than 0 and is in library and if its remove the item
    if 0 <= place < len(library):
        removed = library.pop(place)
        print(f"Removed {removed['title']}\n")
    #else print unvialid number
    else:
        print("Please enter a valid number\n")

#make a funtion for update
def update(library):
    #call check so the user knows what things there are
    check(library)
    #make choice be the number they want to uptdate
    choice = input("What number you want to update: ").strip()
    #if the choice is not digint print to select an actual number and return 
    if not choice.isdigit():
        print("Please enter a valid number\n")
        return
    #make place equals a choice minus one 
    place = int(choice) - 1
    #if the place is not grater than 0 and not in libary print there is an invalid number and return
    if not (0 <= place < len(library)):
        print("Please enter a valid number\n")
        return
    item = library[place]
    #make the user alter the title creator year and genre and make a new string be the choices 
    title = input(f"Title ({item['title']}): ").strip() or item["title"]
    creator = input(f"Creator ({item['creator']}): ").strip() or item["creator"]
    year = input(f"Year ({item['year']}): ").strip() or item["year"]
    genre = input(f"Genre ({item['genre']}): ").strip() or item["genre"]
    #make the place of the library be the dictiory of the title creato year and genre according to the keys 
    library[place] = {"title": title, "creator": creator, "year": year, "genre": genre}
    #print that is updated
    print("item updated\n")

#make a funtion for main 
def main():
    #make library be the funtion load 
    library = load()
    #make a while true loop and print the options 
    while True:
        print("1. Simple list\n2. Detailed list\n3. Add item\n4. Update item\n5. Delete item\n6. Save\n7. Exit")
        #make choice be equals input their choice 
        choice = input("Choice: ").strip()
        #if choice is one, call the check funtion
        if choice == "1":
            check(library)
        #elif choice is 2 then call the show funtion
        elif choice == "2":
            show(library)
        #elif choice is 3 then call the add funtion
        elif choice == "3":
            add(library)
        #elif choice is 4 then call the update funtion
        elif choice == "4":
            update(library)
        #elif choice is 5 then call the delete funtion 
        elif choice == "5":
            delete(library)
        #elif choice is 6 then call the save funtion
        elif choice == "6":
            save(library)
        #elfi choice is 7 ask if they want to safe before leaving 
        elif choice == "7":
            choice = input("Save before exit? (y/n): ").lower()
            #if yes call the save funtion
            if choice == "y":
                save(library)
            #else print to select an actual option and continue
            else:
                print("Please select a valid option")
                continue
            #print that they have decided to exit
            print("You decided to exit")
            break
        #else print to select an actual option and continue
        else:
            print("Please select a valid option")
            continue
#call main
main()