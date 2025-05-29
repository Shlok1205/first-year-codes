temperature=float(input("Enter the temperature in Celsius: "))

if temperature>=30:
    print(f"The temperature is {temperature}°C. It's hot!")
elif 15<temperature<30:
    print(f"The temperature is {temperature}°C. It's warm.")
else:
    print(f"The temperature is {temperature}°C. It's cold.")
