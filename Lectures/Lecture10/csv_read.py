import csv 

filename = "C:\\Users\\chris\\OneDrive\\Документы\\PP2_2025_Spring\\Lectures\\Lecture10\\students.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row) # ['Talgat', '24BD202224', '1', '+77075963428']
                   # ['Aisha', '24BD190836', '1', '+77057403872']
        name, id, study_year, phone_number = row
        print(name, id, study_year, phone_number) # Talgat 24BD202224 1 +77075963428
                                                  # Aisha 24BD190836 1 +77057403872