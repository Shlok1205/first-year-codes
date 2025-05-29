n=int(input("Enter the value: "))
if(n<0):
    print("Invalid input")
# elif (n==0 or n==1):
#     print("Fctorial: 1")
else:
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"Factorial: {factorial}")
print(type(n))
# Enter the value: 5
# Factorial: 120

# Enter the value: 0
# Factorial: 1

# Enter the value: 1
# Factorial: 1

# Enter the value: -6
# Invalid input

# Enter the value: a
# ValueError: invalid literal for int() with base 10: 'a'