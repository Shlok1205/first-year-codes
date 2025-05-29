# # Create a class of student (name, sap id, marks[phy,chem,maths] ). 
# # Create 3 objects by taking inputs from the user and display details of all students.


class student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

# 3 objects by taking user input
students = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    sap_id = input(f"Enter sap_id {i+1}: ")
    marks = {
        "physics": int(input(f"Enter physics marks for {name}: ")),
        "chemistry": int(input(f"Enter chemistry marks for {name}: ")),
        "maths": int(input(f"Enter maths marks for {name}: ")),
    }
    students.append(student(name, sap_id, marks))

# Display the details of each student
print("\nStudent Details:")
for student in students:
    print(f"Name: {student.name}, SAP ID: {student.sap_id}, Marks: {student.marks}")

# -------------------------------------------------------------------------------------------------.

# Add constructor in the above class to initialize student details of n students and implement following methods:
# a)	Display() student details
# b)	Find Marks_percentage() of each student
# c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]
# Write a Function to find average of the class.

class student:
    def _init_(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print(f"Name:{self.name}, SAP ID:{self.sap_id}, marks{self.marks}")

    def marks_percentage(self):
        total_marks = sum(self.marks.values())
        percentage = total_marks/len(self.marks)

    def result(self):
        return "Pass" if all(marks>40 for marks in self.marks.values()) else "Fail"
    
    def average(students):
        total_marks=sum (student.marks_percentage() for students in  students)
        return total_marks/len(students)
    
    # creating and displaying student details
    students = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    sap_id = input(f"Enter sap_id {i+1}: ")
    marks = {
        "physics": int(input(f"Enter physics marks for {name}: ")),
        "chemistry": int(input(f"Enter chemistry marks for {name}: ")),
        "maths": int(input(f"Enter maths marks for {name}: ")),
    }
    students.append(student(name, sap_id, marks))

# Display the details of each student
print("\nStudent Details:")
for student in students:
    print(f"Name: {student.name}, SAP ID: {student.sap_id}, Marks: {student.marks}")
    print(f"Percentage: {student.marks_percentage()}")
    print(f"Result: {student.result()}")

# -------------------------------------------------------------------------------------------------.

# Create programs to implement different types of inheritances.

class Model:
    def train(self):
        print('Training the generic model.')

class LinearRegression(Model):
    def train(self):
        print('Training the linear regression model.')
        Model.train(self)
# Usage:
model = LinearRegression()
model.train()

# Multiple
class Regression:
    def type(self):
        print("I am a regression model.")

class Classification:
    def category():
        print("I am a classification model.")

class HybridModel(Regression, Classification):
    def info(self):
        print("I can perform both Regression and Classification.")

# Usage:
hybrid = HybridModel()
hybrid.type()
hybrid.category()
hybrid.info()


# Multilevel Inheritance
class MLModel:
    def info(self):
        print("General ML model.")

class NeuralNetwork(MLModel):
    def layers(self):
        print("Neural Network has layers.")

class CNN(NeuralNetwork):
    def convolutional_layer(self):
        print("CNN includes convolutional layers.")

# Usage:
cnn = CNN()
cnn.info()
cnn.layers()
cnn.convolutional_layer()

# -------------------------------------------------------------------------------------------------

#Create a class to implement method Overriding

class parent:
    def show(self):
        print("Parent class")

class child(parent):
    def show(self):
        print("Child class method overriding parent class method")

# usage
child=child()
child.show()

# -------------------------------------------------------------------------------------------------

# Create a class for operator overloading which adds two Point Objects where Point has x & y values
# e.g. if
# P1(x=10,y=20)
# P2(x=12,y=15)
# P3=P1+P2 => P3(x=22,y=35)

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

def add(self, other):
    return Point(self.x + other.x,self.y + other.y)

def _str_(self):
    return f"Point({self.x},{self.y})"

P1=Point(10,20)
P2=Point(12,15)
P3=P1+P2
print(P3)       