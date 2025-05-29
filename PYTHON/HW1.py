#Write a program to calculate total amount of money in a piggybank given the coins of 10,5,2,1 
def calculate_total_amount():
    rupees_10=int(input("Enter the number of 10 rupee coins: "))
    rupees_5=int(input("Enter the number of 5 rupee coins: "))
    rupees_2=int(input("Enter the number of 2 rupee coins: "))
    rupees_1=int(input("Enter the number of 1 rupee coins: "))

    total_amount=(rupees_10*10)+(rupees_5*5)+(rupees_2*2)+(rupees_1*1)

    print(f"Total amount in the piggybank: Rs. {total_amount}")

calculate_total_amount()

#Enter the number of 10 rupee coins: 10
#Enter the number of 5 rupee coins: 10
#Enter the number of 2 rupee coins: 5
#Enter the number of 1 rupee coins: 10
#Total amount in the piggybank: Rs. 170