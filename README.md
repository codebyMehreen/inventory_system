
📦 Inventory Management System
A simple and interactive inventory management tool built with Python. It allows users to manage items with details like quantity, category, and description, and supports saving/loading data in JSON and CSV formats.

🚀 Features
- ✅ Add new items to inventory
- ❌ Remove items or entire entries
- 📋 View current inventory list
- 🔍 Search for specific items
- 💾 Save inventory to a JSON file
- 📂 Load inventory from a JSON file
- 📤 Export inventory to a CSV file
- 📥 Import inventory from a CSV file
- 🧭 Menu-driven interface for easy navigation

🛠️ Requirements
- Python 3.x
- No external libraries required (uses built-in modules: json, os, csv)

📂 File Structure
inventory_system.py  # Main script containing all functionality
inventory.json       # (Optional) JSON file for saving/loading data
inventory.csv        # (Optional) CSV file for exporting/importing data



▶️ How to Run
- Make sure you have Python installed.
- Save the script as inventory_system.py.
- Open a terminal or command prompt.
- Run the script:
python inventory_system.py


- Follow the on-screen menu to manage your inventory.

📌 Example Usage
- Add an item:
Enter item name: Apple
Enter quantity: 10
Enter category: Fruit
Enter description: Fresh red apples
- Remove an item:
Enter item name: Apple
Enter quantity to remove: 5
- Export to CSV:
Saves inventory to inventory.csv for external use.

📎 Notes
- The system automatically updates quantities if an item already exists.
- Removing more items than available will trigger a warning.
- JSON and CSV files are created in the same directory as the script.

📧 Contact
For questions or suggestions, feel free to reach out or fork the project to enhance it further!


