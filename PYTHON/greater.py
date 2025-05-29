a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))

if a>=b and a>=c:
    print(f"The greatest number is: {a}")
elif b>=a and b>=c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")