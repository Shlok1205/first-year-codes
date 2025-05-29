a=float(input("Enter a number: "))
b=float(input("Enter another number: "))

try:
    result = a/b
    
except ZeroDivisionError:
    print("Division by zero is not possible")

except ValueError:
    print("Please enter a valid input")

except Exception as e:
    print(f"Brotha {e}")

else:
    print(result)

finally:
    print("Mission Accomplish!")