a= int (input("Enter first number= "))
b= int (input("Enter second number= "))
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice=input("Enter the number of your choice (1/2/3/4): ")
if choice=='1':
    result=a+b
    print(f"The result of addition is: {a+b}")
elif choice=='2':
    result=b-a
    print(f"The result of subtraction is: {b-a}")
elif choice=='3':
    result=a*b
    print(f"The result of multiplication is: {a*b}")
elif choice=='4':
    if b!=0:
        result=a/b
        print(f"The result of division is: {a/b}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")