import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["NAME", "Age", "Grade"])
    writer.writerow(["Alice", 14, "8th"])
    writer.writerow(["BOB", 15, "9th"])
    writer.writerow(["Charlie", 16, "10th"])

    
import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)