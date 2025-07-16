import json
import os
import csv

# Inventory: {item_name: {"quantity": int, "category": str, "description": str}}
inventory = {}

# Add item
def add_item(name: str, quantity: int, category: str, description: str) -> None:
    if name in inventory:
        inventory[name]["quantity"] += quantity
    else:
        inventory[name] = {
            "quantity": quantity,
            "category": category,
            "description": description
        }
    print(f"✅ Added: {quantity} x {name} ({category})")

# Remove item
def remove_item(name: str, quantity: int) -> None:
    if name in inventory:
        if inventory[name]["quantity"] > quantity:
            inventory[name]["quantity"] -= quantity
            print(f"❌ Removed: {quantity} x {name}")
        elif inventory[name]["quantity"] == quantity:
            del inventory[name]
            print(f"❌ Removed all of: {name}")
        else:
            print(f"⚠️ Not enough quantity to remove. You have {inventory[name]['quantity']}")
    else:
        print(f"⚠️ Item not found: {name}")

# View inventory
def view_inventory() -> None:
    print("\n📋 Inventory List:")
    if inventory:
        for name, info in inventory.items():
            print(f"- {name}: {info['quantity']} ({info['category']})")
    else:
        print("Inventory is empty.")
    print()

# Search item
def search_item(name: str) -> None:
    print(f"\n🔍 Searching for: {name}")
    if name in inventory:
        info = inventory[name]
        print(f"✅ Found: {name}")
        print(f"Quantity: {info['quantity']}")
        print(f"Category: {info['category']}")
        print(f"Description: {info['description']}")
    else:
        print("❌ Item not found.")
    print()

# Save to JSON
def save_inventory_json(filename: str = "inventory.json") -> None:
    with open(filename, "w") as file:
        json.dump(inventory, file)
    print(f"💾 Inventory saved to {filename}")

# Load from JSON
def load_inventory_json(filename: str = "inventory.json") -> None:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            inventory.clear()
            inventory.update(data)
        print(f"📂 Inventory loaded from {filename}")
    else:
        print(f"⚠️ File not found: {filename}")

# Export to CSV
def export_inventory_csv(filename: str = "inventory.csv") -> None:
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Quantity", "Category", "Description"])
        for name, info in inventory.items():
            writer.writerow([name, info["quantity"], info["category"], info["description"]])
    print(f"📤 Inventory exported to {filename}")

# Import from CSV
def import_inventory_csv(filename: str = "inventory.csv") -> None:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            inventory.clear()
            for row in reader:
                inventory[row["Name"]] = {
                    "quantity": int(row["Quantity"]),
                    "category": row["Category"],
                    "description": row["Description"]
                }
        print(f"📥 Inventory imported from {filename}")
    else:
        print(f"⚠️ File not found: {filename}")

# Menu loop
def run_inventory_system():
    while True:
        print("\n📦 Inventory System Menu")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Export to CSV")
        print("8. Import from CSV")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_item(name, quantity, category, description)
        elif choice == "2":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(name, quantity)
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            name = input("Enter item name to search: ")
            search_item(name)
        elif choice == "5":
            save_inventory_json()
        elif choice == "6":
            load_inventory_json()
        elif choice == "7":
            export_inventory_csv()
        elif choice == "8":
            import_inventory_csv()
        elif choice == "9":
            print("👋 Exiting Inventory System. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter a number from 1 to 9.")

# Run the program

run_inventory_system()

#WebDevelopment #FrontendDev #JavaScript #HTML #CSS #GitHubPages #WomenInTech #PortfolioProject #LinkedInTech #RecipeApp
