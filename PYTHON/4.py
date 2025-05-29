try:
    a = float(input("Enter the first number: ").strip())
    b = float(input("Enter the second number: ").strip())
    c = float(input("Enter the third number: ").strip())

    if a>=b and a>=c:
        if a.is_integer():
            print("The greatest number is:", int(a))
        else:
            print("The greatest number is:", a)
    elif b>=a and b>=c:
        if b.is_integer():
            print("The greatest number is:", int(b))
        else:
            print("The greatest number is:", b)
    elif c>=a and c>=b:
        if c.is_integer():
            print("The greatest number is:", int(c))
        else:
            print("The greatest number is:", c)
    else:
        print("Unexpected error!")

except ValueError:
    print("Invalid input. Please enter numeric values only.")