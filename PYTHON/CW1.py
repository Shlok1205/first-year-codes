# scan n values in range 0 to 3 and print the number of times each value has occured

# def count_occurrence(n):
#     d = {i: 0 for i in range(4)}  
#     print(f"Enter {n} values between 0 and 3:")
#     for _ in range(n):
#         value = int(input())
#         if 0 <= value <= 3:
#             d[value] += 1
#         else:
#             print(f"Value {value} is out of range and will not be counted.")
    
#     print("Occurrences:", d)
#     print(type(d))

# n = int(input("Enter the number of values: "))
# count_occurrence(n)

# in float

# --------------------------------------------------------------------------------------

# Create a tuple to store n numeric values and find average of all values

# def average_of_values(n):
#     print(f"Enter {n} numeric values: ")
#     values: tuple= tuple(float(input()) for i in range(n))
#     print(f"Values: {values}")
#     print(f"Average: {sum(values)/n}")
# print("Enter the number of values: ")
# n = int(input())
# average_of_values(n)

#---------------------------------------------------------------------------------------




def runner_up():
    n = 5
    
    scores = list(map(int, input("Enter wickets taken by 5 bowlers, separated by ',': \n").split(",")))
    if len(scores) != n:
        print("Please enter exactly 5 scores.")
        return
    if any(score > 10 for score in scores):
        print("Each bowler can take a maximum of 10 wickets.")
        return
    
    scores.sort()
    print("Sorted Wickets:", scores)
    print("Runner-up Wickets:", scores[-2])

runner_up()

# ---------------------------------------------------------------------------------------

