#ES 1rst Movie recomendations
#import csv
import csv 
try:
    with open("Notes\Class_CSV_sample.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        row = []
        for line in content:
            row.append({headers[0]: line[0], headers[1]: line[1]})
except:
    print("cnat find the cvs")
else:
    for line in row:
        print(line)

#make funtion for search or recomentadation
def search():
    print("ji")



#make a funtion for print full movie
def print_movie():
    print("hj")




#make a funtion for main
def main():
    #make a while loop and make choice equals an input of what they want to do 
    while True:
        choice = input("")
    #if choice is one call search

    #if choice is two call print movie

    #if choice is three break 

    #else print to select an actual option