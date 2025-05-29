#Write a program to bill amount for an item given its quantity, sold, valued, discount and taxes
def calculate_bill():
    quantity = int(input("Enter the quantity of the item: "))
    sold_value_per_item = float(input("Enter the sold value per item (Rs.): "))
    discount_percent = float(input("Enter the discount percentage: "))
    tax_percent = float(input("Enter the tax percentage: "))

    total_sold_value = quantity * sold_value_per_item

    discount_amount = (discount_percent / 100) * total_sold_value

    taxable_amount = total_sold_value - discount_amount

    tax_amount = (tax_percent / 100) * taxable_amount

    final_bill_amount = taxable_amount + tax_amount

    print("\n--- Bill Breakdown ---")
    print(f"Total Sold Value: Rs. {total_sold_value:.2f}")
    print(f"Discount Amount: Rs. {discount_amount:.2f}")
    print(f"Taxable Amount: Rs. {taxable_amount:.2f}")
    print(f"Tax Amount: Rs. {tax_amount:.2f}")
    print(f"Final Bill Amount: Rs. {final_bill_amount:.2f}")

calculate_bill()

#---Enter the quantity of the item: 5
#Enter the sold value per item (Rs.): 50
#Enter the discount percentage: 10
#Enter the tax percentage: 12.3

#--- Bill Breakdown ---
#Total Sold Value: Rs. 250.00
#Discount Amount: Rs. 25.00
#Taxable Amount: Rs. 225.00
#Tax Amount: Rs. 27.68
#Final Bill Amount: Rs. 252.68