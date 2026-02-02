#ES 1 reading list

import csv
while True:
    try:
        with open("Notes/create_list.txt", "r") as file:
            for line in file:
                print(line.strip())
    except:
        print("that file can't be found")
    else:
        print("code ends")
        break

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