import csv

# Sample data
students = [
    ["Name", "RollNo", "Marks"],
    ["Aayush", "3", "85"],
    ["Subash", "24", "70"],
    ["Sandesh", "103", "78"]
]

# Write data to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file 'students.csv' created and data written successfully.")

import csv

# Read data from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)  # Each row is a list of values
