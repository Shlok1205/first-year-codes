# WAP to print first n numbners

# n = int(input("Enter the value of n: "))

# print("The first",n,"numbers are: ")

# for i in range(1,n+1):
#     print(i,end=" ")

# -----------------------------------------------------------------

# lambde

# r, h = map(float, input("Values of r and h: ").split()) 
# volume_of_cone = lambda r, h: (1/3) * 3.14 * r * r * h
# print("Volume of cone: {:.2f}".format(volume_of_cone(r, h)))

# -----------------------------------------------------------------

# sum of the cube of all the positive integers smaller than the specified number. 
# def sum_of_cubes(n):
#     return sum(map(lambda x: x**3, range(1, n)))
#     # return sum(filter(None, (x**3 for x in range(1, n))))

# number = 5
# result = sum_of_cubes(number)
# print(f"Sum of the cubes of all positive integers smaller than {number} is {result}")


#------------------------------------------------------------------

# Sum of cubes

# def sum_of_cubes(n):

#     if n <= 0:
#         return "Please enter a positive integer."
#     return sum(i**3 for i in range(1, n))

# number = int(input("Integer: "))
# result = sum_of_cubes(number)
# print(f"The sum of cubes of all positive integers smaller than {number} is: {result}")

# -----------------------------------------------------------------

# Fibonacci

# def fibonacci_series(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#     print()

# n = int(input("Number of terms: "))
# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci Series:")
#     fibonacci_series(n)

# -----------------------------------------------------------------

# tuple of max and min

# get_max_min = lambda lst: (max(lst), min(lst))

# sample_list = [10, 6, 8, 90, 12, 56]
# result = get_max_min(sample_list)

# print("Max and Min as a tuple:", result)


# -----------------------------------------------------------------

# Initialize dictionaries for students
students = {}

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Name: ")
    grade = input("Grade: ")
    marks = float(input("Marks: "))
    students[f"student{i + 1}"] = {"name": name, "grade": grade, "marks": marks}

assignment_list = []
pass_list = []

for student_id, details in students.items():
    if details["marks"] < 50:
        assignment_list.append({"name": details["name"], "grade": details["grade"]})
    else:
        pass_list.append({"name": details["name"], "grade": details["grade"]})

# Display results
print("\nStudents getting an assignment:")
for student in assignment_list:
    print(student)

print("\nStudents who cleared exam:")
for student in pass_list:
    print(student)




