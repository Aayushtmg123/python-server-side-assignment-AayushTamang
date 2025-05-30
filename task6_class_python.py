# Define a Student class
class Student:
    # This function runs when we create a new student
    def own(self):
        self.name = ""
        self.roll = ""
        self.number = ""
        self.marks = 0.0

    # Function to input student details from the user
    def input_details(self):
        self.name = input("Enter student's name: ")
        self.roll = input("Enter roll number: ")
        self.number = input("Enter contact number: ")
        self.marks = float(input("Enter marks: "))

    # Function to display student details
    def display_details(self):
        print("\n--- Student Details ---")
        print("Name          :", self.name)
        print("Roll Number   :", self.roll)
        print("Contact Number:", self.number)
        print("Marks         :", self.marks)

# Create a student object
student1 = Student()

# Call the method to input details
student1.input_details()

# Call the method to display details
student1.display_details()
