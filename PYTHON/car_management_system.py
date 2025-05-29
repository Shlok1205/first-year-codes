# Car Management System

def display_cars(car_data):
    """Displays all available car companies, products, and colours."""
    if not car_data:
        print("\nNo data available.")
        return
    print("\nAvailable Cars:")
    for key, value in car_data.items():
        print(f"\nCompany: {value['Company']}")
        print(f"Products: {', '.join(value['Product'])}")
        print(f"Colours: {', '.join(value['Colour'])}")

def add_car(car_data):
    """Adds a new car entry."""
    company = input("Enter company name: ").strip()
    if company in car_data:
        print("This company already exists!")
        return
    product = input("Enter product names (comma-separated): ").strip().split(", ")
    colour = input("Enter colour options (comma-separated): ").strip().split(", ")
    car_data[company] = {"Company": company, "Product": product, "Colour": colour}
    print(f"{company} added successfully!")

def remove_car(car_data):
    """Removes a car company from the data."""
    company = input("Enter company name to remove: ").strip()
    if company in car_data:
        del car_data[company]
        print(f"{company} removed successfully!")
    else:
        print("Company not found!")

def update_car(car_data):
    """Updates product and colour details for a car company."""
    company = input("Enter company name to update: ").strip()
    if company in car_data:
        product = input("Enter updated product names (comma-separated): ").strip().split(", ")
        colour = input("Enter updated colour options (comma-separated): ").strip().split(", ")
        car_data[company].update({"Product": product, "Colour": colour})
        print(f"{company} updated successfully!")
    else:
        print("Company not found!")

def pop_colour(car_data):
    """Removes the colour options of a car company."""
    company = input("Enter company name: ").strip()
    if company in car_data:
        print(f"Removed Colours: {car_data[company].pop('Colour', 'No Colours Found')}")
    else:
        print("Company not found!")

def main():
    car_data = {
        "Maruti": {"Company": "Maruti", "Product": ["Alto", "WagonR", "Swift"], "Colour": ["Red", "Blue", "White"]},
        "Hyundai": {"Company": "Hyundai", "Product": ["i10", "i20", "Verna"], "Colour": ["Red", "Blue", "White"]},
        "Kia": {"Company": "Kia", "Product": ["Seltos", "Sonet", "Carnival"], "Colour": ["Red", "Blue", "White"]},
    }
    
    while True:
        print("\nMenu:")
        print("1. Add Car")
        print("2. Display Cars")
        print("3. Remove Car")
        print("4. Clear All Data")
        print("5. Remove Last Entry")
        print("6. Update Car Details")
        print("7. Pop Colour")
        print("8. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_car(car_data)
        elif choice == "2":
            display_cars(car_data)
        elif choice == "3":
            remove_car(car_data)
        elif choice == "4":
            car_data.clear()
            print("All data cleared.")
        elif choice == "5":
            if car_data:
                removed_item = car_data.popitem()
                print(f"Removed: {removed_item}")
            else:
                print("No data to remove.")
        elif choice == "6":
            update_car(car_data)
        elif choice == "7":
            pop_colour(car_data)
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
