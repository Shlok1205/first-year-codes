def lcm(a, b):
    #WAP to find the LCM of two numbers.
    a, b = abs(a), abs(b)
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i

def is_armstrong(num):
    #WAP to check if a number is Armstrong.
    num_str = str(num)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == num, num_digits

def fibonacci_series(n):
    #WAP to generate Fibonacci series.
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def is_prime(n):
    #WAP to check if a number is prime or not.
    return "P" if n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)) else "NP"

def is_palindrome(num):
    #WAP to check if a number is a palindrome.
    clean_num = str(abs(num))
    return clean_num == clean_num[::-1], len(clean_num)

def sum_of_digits(number):
    #WAP to calculate the sum of digits.
    return sum(int(i) for i in str(abs(int(number))))

def get_divisible_numbers(start, end):
    #WAP to print numbers divisible by 5 and 7 between 1 to 100.
    return [num for num in range(start, end + 1) if num % 5 == 0 and num % 7 == 0]

def swap_case(string):
    #WAP to convert string to swapcase.
    return string.swapcase()

def print_table(num, limit):
    #WAP to print multiplication table of a number.
    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")

def menu():
    #Menu driven program.
    while True:
        print("\nMenu:")
        print("1. Find the LCM of two numbers")
        print("2. Check if a number is Armstrong")
        print("3. Generate Fibonacci series")
        print("4. Check if a number is prime")
        print("5. Check if a number is a palindrome")
        print("6. Calculate the sum of digits")
        print("7. Print numbers divisible by 5 and 7 between 1 to 100")
        print("8. Convert string to swapcase")
        print("9. Print multiplication table of a number")
        print("10. Exit")

        choice = input("Enter your choice: ") #Taking user input

        if choice == "1": #LCM
            while True:
                try:
                    a, b = float(input("Enter the first number: ")), float(input("Enter the second number: "))
                    if a.is_integer() and b.is_integer():
                        print(f"LCM of {int(a)} and {int(b)} is {lcm(int(a), int(b))}")
                    else:
                        print("LCM is only defined for whole numbers.")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "2": #Armstrong
            while True:
                try:
                    number = float(input("Enter a number: "))
                    if number.is_integer():
                        result, count = is_armstrong(int(number))
                        print(f"Number of digits: {count}\n{int(number)} is {'an Armstrong number' if result else 'not an Armstrong number'}.")
                    else:
                        print("Armstrong check works only for whole numbers.")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "3": #Fibonacci
            while True:
                try:
                    n = int(input("Enter the number of Fibonacci values to display: "))
                    if n > 0:
                        fibonacci_series(n)
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "4": #Prime
            while True:
                try:
                    num = float(input("Enter a number: "))
                    if num.is_integer():
                        print(is_prime(int(num)))
                    else:
                        print("Prime check works only for whole numbers.")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "5": #Palindrome
            while True:
                try:
                    num = input("Enter a number: ")
                    float(num)
                    is_pal, length = is_palindrome(int(num))
                    print(f"{num} is {'a palindrome' if is_pal else 'not a palindrome'} with {length} characters.")
                    
                    string = input("Enter a word or sentence: ")
                    refined_str = "".join(char for char in string if char != " ")
                    print(f"The refined string is: {refined_str}")
                    print("Yes, it's a palindrome." if refined_str == refined_str[::-1] else "No, it's not a palindrome.")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "6": #Sum of digits
            while True:
                try:
                    number = float(input("Enter the number: "))
                    print(f"Sum of digits: {sum_of_digits(number)}")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "7": #Divisible numbers
            while True:
                divisible_numbers = get_divisible_numbers(1, 100)
                choice = input("Enter what to print (first 10, last 10, between 20): ").strip().lower()
                if choice == "first 10":
                    print("First 10 numbers divisible by 5 and 7:", divisible_numbers[:10])
                elif choice == "last 10":
                    print("Last 10 numbers divisible by 5 and 7:", divisible_numbers[-10:])
                elif choice == "between 20" and len(divisible_numbers) > 20:
                    print("Between 20 numbers:", divisible_numbers[len(divisible_numbers)//2 - 10 : len(divisible_numbers)//2 + 10])
                else:
                    print("Invalid choice")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "8": #Swapcase
            while True:
                string = input("Enter a string: ")
                print(f"Converted string: {swap_case(string)}")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "9": #Multiplication table
            while True:
                try:
                    num = float(input("Enter the number: "))
                    limit = int(input(f"Enter the limit till when you want the table of {int(num)} to be printed: "))
                    print_table(int(num), limit)
                    while True:
                        query = input("Enter a multiplication query or type 'stop' to exit: ").strip()
                        if query.lower() == "stop":
                            break
                        try:
                            a, b = map(int, query.split('*'))
                            print(f"{a} x {b} = {a * b}")
                        except:
                            print("Invalid input")
                except ValueError:
                    print("Invalid input")
                if input("Type 'stop' to exit or press Enter to continue: ").lower() == "stop":
                    break

        elif choice == "10":
            print("Exiting program!Byeeeeeeee!") #Exiting the program
            break

        else:
            print("Invalid choice") #Invalid choice

#Calling the menu function
if __name__ == "__main__":
    menu()
