#inputting students name
students=[]
n = int(input("How many Students You want?\n"))

for i in range(n):
    name=input(f"Enter the name of student{i+1}:")
    students.append(name)

#writing name in file
with open("students.txt","w") as f:
    for student in students:
        f.write(student + "\n")

#Read and display file contents
print("\n Stored contents are:")
with open("students.txt","r") as f:
    for student in students:
       print(f.read())