# Tennyson data

def display_aliens(alien_data):
    """Displays all available aliens."""
    if not alien_data:
        print("\nNo aliens available.")
        return
    print("\nAvailable Aliens:")
    for key, value in alien_data.items():
        print(f"\nAlien: {value['Name']}")
        print(f"Species: {value['Species']}")
        print(f"Home Planet: {value['Home Planet']}")

def add_alien(alien_data):
    """Adds a new alien entry."""
    name = input("Enter alien name: ").strip()
    if name in alien_data:
        print("This alien already exists!")
        return
    species = input("Enter species: ").strip()
    planet = input("Enter home planet: ").strip()
    alien_data[name] = {"Name": name, "Species": species, "Home Planet": planet}
    print(f"{name} added successfully!")

def remove_alien(alien_data):
    """Removes an alien."""
    name = input("Enter alien name to remove: ").strip()
    if name in alien_data:
        del alien_data[name]
        print(f"{name} removed successfully!")
    else:
        print("Alien not found!")

def pop_alien(alien_data):
    """Removes the last added alien."""
    if alien_data:
        removed_item = alien_data.popitem()
        print(f"Removed: {removed_item}")
    else:
        print("No aliens to remove.")

def main():
    alien_data = {
        "Heatblast": {"Name": "Heatblast", "Species": "Pyronite", "Home Planet": "Pyros"},
        "XLR8": {"Name": "XLR8", "Species": "Kineceleran", "Home Planet": "Kinet"},
        "Four Arms": {"Name": "Four Arms", "Species": "Tetramand", "Home Planet": "Khoros"},
        "Grey Matter": {"Name": "Grey Matter", "Species": "Galvan", "Home Planet": "Galvan Prime"},
        "Diamondhead": {"Name": "Diamondhead", "Species": "Petrosapien", "Home Planet": "Petropia"},
        "Wildmutt": {"Name": "Wildmutt", "Species": "Vulpimancer", "Home Planet": "Vulpin"},
        "Ripjaws": {"Name": "Ripjaws", "Species": "Piscciss Volann", "Home Planet": "Piscciss"},
        "Stinkfly": {"Name": "Stinkfly", "Species": "Lepidopterran", "Home Planet": "Lepidopterra"},
        "Upgrade": {"Name": "Upgrade", "Species": "Galvanic Mechamorph", "Home Planet": "Galvan B"},
        "Ghostfreak": {"Name": "Ghostfreak", "Species": "Ectonurite", "Home Planet": "Anur Phaetos"},
    }
    
    creator = "Azmuth"
    wielder = "Ben Tennyson"
    organization = "The Plumbers"
    
    villains = {
        "Vilgax",
        "Dr. Animo",
        "Charmcaster",
        "Forever Knights",
        "Kevin 11",
        "Zombozo",
        "Hex",
        "DNAliens",
        "Highbreed",
    }
    
    while True:
        print("\nMenu:")
        print("1. Add Alien")
        print("2. Display Aliens")
        print("3. Remove Alien")
        print("4. Remove Last Alien")
        print("5. Show Villains")
        print("6. Show Omnitrix Details")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_alien(alien_data)
        elif choice == "2":
            display_aliens(alien_data)
        elif choice == "3":
            remove_alien(alien_data)
        elif choice == "4":
            pop_alien(alien_data)
        elif choice == "5":
            print("\nVillains Ben has faced:")
            for villain, desc in villains.items():
                print(f"{villain}: {desc}")
        elif choice == "6":
            print("\nOmnitrix Details:")
            print(f"Creator: {creator}")
            print(f"Wielder: {wielder}")
            print(f"Organization: {organization}")
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
    
