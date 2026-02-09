#ES 1 writing files\

#with open("Notes/create_list.txt", "r+") as file:
    #content = file.read()
    #content += "\n I wrote on my file"
    #file.write("I wrote on my file")



#with open ("Notes/create_list.txt", "a") as file:
    #file.write("\nthis is more on my file")


#print("code ended")


import csv 

with open("Notes/class_sample.csv", "r+", newline='') as csvfile:
    fieldnames = ['username','color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}, {line[0]} favorite color {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'aUser', 'color': 'pink'})
    writer.writerow({'username': 'yo', 'color': 'hotpink'})
    writer.writerow({'username': 'someoneelse', 'color': 'red'})
    writer.writerow({'username': 'me', 'color': 'blue'})

print("code is done")