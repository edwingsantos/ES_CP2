#import csv
import csv
#make a funtion for loading the movies
def load_movies():
    #open the csv file and read it with the r, as f
    with open("Individual_projects/movies.csv", "r") as f:
        #read all the things in the file
        reader = csv.DictReader(f)
        movies = list(reader)
        #print how many movies there are
    print(f"{len(movies)} movies founded")
    return movies
#make a funtion for genre
def genre_things(movies, genre):
    #make genre be lower and return the genre in movies and check if its not in there, then return all the movies with the genre in it
    genre = genre.lower().strip()
    filtered = [m for m in movies if genre in m["Genre"].lower()]
    if not filtered:
        print("that genre is not on")
    return filtered
#make another funtion for director and do the same as above
def director(movies, director):
    director = director.lower().strip()
    return [m for m in movies if director in m["Director"].lower()]
#make a funtion but for actor and do the same above
def actor(movies, actor):
    actor = actor.lower().strip()
    return [m for m in movies if actor in m["Notable Actors"].lower()]
#make a funtion for lenght and do the same as above
def length(movies, min_len=None, max_len=None):
    result = []
    for m in movies:
        try:
            length = int(m["Length (min)"])
        except:
            continue
        if min_len and length < min_len:
            continue
        if max_len and length > max_len:
            continue
        result.append(m)
    return result
#Make a funtion called filter rating and do the same a above
def filter_rating(movies, rating):
    rating = rating.lower().strip()
    return [m for m in movies if rating == m["Rating"].lower().strip()]
#make a funtion for movie seach
def search_movies(movies):
    #make a while true loop to stupid prove the quiestion
    while True:
        choice = input("1. Genre\n2. Director\n3. Actor\n4. Length (min/max)\n5. Rating (PG, PG-13, R, etc.)").strip()
        #make something be the movies and display the choices
        filtered = movies
        choices = [c.strip() for c in choice.split(",")]
        #if 1 is in choice enter the genre and make filtered the genre things
        if "1" in choices:
            genre = input("Enter genre: ")
            filtered = genre_things(filtered, genre)
        #if 2 is in choice enter the director and make filtered director function 
        if "2" in choices:
            director_name = input("Enter director: ")
            filtered = director(filtered, director_name)
        # if 3 is in choices the enter the actor and make filtered the actor funtion
        if "3" in choices:
            actor_name = input("Enter actor: ")
            filtered = actor(filtered, actor_name)
        #if 4 in choice make the user choose the min and max 
        if "4" in choices:
            min_input = input("Enter minimum length: ").strip()
            max_input = input("Enter maximum length: ").strip()
            #if the user didnt choose a digit select that make it a digit
            if not min_input.isdigit() or not max_input.isdigit():
                print("is not a digit, please select again")
            #make if the choice is not an integer then make it nothing, then call main
            min_len = int(min_input) if min_input.isdigit() else None
            max_len = int(max_input) if max_input.isdigit() else None
            filtered = length(filtered, min_len, max_len)
            main()
        #if 5 in choices make the user choose the rating and make filterid be the filter rating function
        if "5" in choices:
            rating = input("Enter rating (PG, PG-13, R, etc.): ")
            filtered = filter_rating(filtered, rating)
        #if filtered is true print the resuslt in a organized way. else print that the movies dont match 
        if filtered:
            print("\nResults:")
            for idx, m in enumerate(filtered, 1):
                print(f"{idx}. {m['Title']} — {m['Genre']} — {m['Director']} — {m['Notable Actors']} — {m['Length (min)']} min — {m['Rating']}")
        else:
            print("No movies match those filters.")
        #make agian be if they want to search agian, if y break
        again = input("\nSearch again? (y/n): ").lower().strip()
        if again == "y":
            break
#make a funtion for printing movies 
def print_movies(movies):
    print("\nFull Movie List:")
    #make a loop with index and enumerate and print it in a way that seems organized 
    for idx, m in enumerate(movies, 1):
        print(f"{idx}. {m['Title']} — {m['Genre']} — {m['Director']} — {m['Notable Actors']} — {m['Length (min)']} min — {m['Rating']}")
    input("\nPress Enter to return to main menu.")
#make a funtion for main
def main():
    movies = load_movies()
    #make a while true loop and make choice be where they want to go 
    while True:
        print("\nMain Menu:")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")
        choice = input("Choice: ").strip()
        #if choice is 1 call seach movies
        if choice == "1":
            search_movies(movies)
        #if choice 2 call the print movies 
        elif choice == "2":
            print_movies(movies)
        #if 3 break
        elif choice == "3":
            break
        #else print to use an actual option
        else:
            print("Please select an actual option")




# Run program
if __name__ == "__main__":
    main()
