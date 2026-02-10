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
def genre(movies, genre):
    #make genre be lower and return the genre in movies and check if its not in there
    genre = genre.lower().strip()
    if genre not in movies:
        print("that genre is not on")
    return [m for m in movies if genre in m["Genre"].lower()]

def director(movies, director):
    director = director.lower().strip()
    return [m for m in movies if director in m["Director"].lower()]

def actor(movies, actor):
    actor = actor.lower().strip()
    return [m for m in movies if actor in m["Notable Actors"].lower()]

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

def filter_rating(movies, rating):
    rating = rating.lower().strip()
    return [m for m in movies if rating == m["Rating"].lower().strip()]

# ---------- SEARCH ----------
def search_movies(movies):
    while True:
        print("1. Genre")
        print("2. Director")
        print("3. Actor")
        print("4. Length (min/max)")
        print("5. Rating (PG, PG-13, R, etc.)")
        choice = input("Selected filters: ").strip()


        filtered = movies
        choices = [c.strip() for c in choice.split(",")]

        if "1" in choices:
            genre = input("Enter genre: ")
            filtered = genre(filtered, genre)
        elif "2" in choices:
            director = input("Enter director: ")
            filtered = director(filtered, director)
        elif "3" in choices:
            actor = input("Enter actor: ")
            filtered = actor(filtered, actor)
        elif "4" in choices:
            min_input = input("Enter minimum length: ").strip()
            max_input = input("Enter maximum length: ").strip()
            min_len = int(min_input) if min_input.isdigit() else None
            max_len = int(max_input) if max_input.isdigit() else None
            filtered = length(filtered, min_len, max_len)
        elif "5" in choices:
            rating = input("Enter rating (PG, PG-13, R, etc.): ")
            filtered = filter_rating(filtered, rating)

        elif filtered:
            print("\nResults:")
            for idx, m in enumerate(filtered, 1):
                print(f"{idx}. {m['Title']} — {m['Genre']} — {m['Director']} — {m['Notable Actors']} — {m['Length (min)']} min — {m['Rating']}")
        else:
            print("No movies match those filters.")

        again = input("\nSearch again? (y/n): ").lower().strip()
        if again == "y":
           continue

# ---------- PRINT ALL ----------
def print_movies(movies):
    print("\nFull Movie List:")
    for idx, m in enumerate(movies, 1):
        print(f"{idx}. {m['Title']} — {m['Genre']} — {m['Director']} — {m['Notable Actors']} — {m['Length (min)']} min — {m['Rating']}")
    input("\nPress Enter to return to main menu.")

# ---------- MAIN ----------
def main():
    movies = load_movies()

    while True:
        print("\nMain Menu:")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            search_movies(movies)
        elif choice == "2":
            print_movies(movies)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")

# Run program
main()
