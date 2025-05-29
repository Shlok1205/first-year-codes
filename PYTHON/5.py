value = float(16 / 3)  

print("Original value (float):", value)
print("Rounded to 2 decimal places:", format(value, '.2f'))
print("No decimal places (float):", format(value, '0f'))
print("Rounded to whole number (float):", format(value, '.0f'))
print("Rounded to 4 decimal places (float):", format(value, '.4f'))
print("Rounded to 6 decimal places (float):", format(value, '.6f'))

#Original value (float): 5.333333333333333
#Rounded to 2 decimal places: 5.33
#No decimal places (float): 5.333333
#Rounded to whole number (float): 5
#Rounded to 4 decimal places (float): 5.3333
#Rounded to 6 decimal places (float): 5.333333