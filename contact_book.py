import json
import os

# Define file name for persistent data storage
DATA_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from a JSON file, or returns an empty dictionary."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Warning: Data file corrupted. Starting with an empty list.")
        return {}

def save_contacts(contacts):
    """Saves the current contacts dictionary to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(contacts, file, indent=4)
    except IOError:
        print("❌ Error: Could not save data to disk.")

def add_contact(contacts):
    """Adds a new contact to the directory."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("❌ Error: Name cannot be blank.")
        return
    
    if name in contacts:
        print(f"❌ Error: A contact named '{name}' already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Lists all stored contacts."""
    if not contacts:
        print("📂 The contact book is currently empty.")
        return
    
    print("\n" + "="*40)
    print(f"{'NAME':<15} | {'PHONE':<15} | {'EMAIL'}")
    print("="*40)
    for name, info in contacts.items():
        print(f"{name:<15} | {info['phone']:<15} | {info['email']}")
    print("="*40)

def search_contact(contacts):
    """Searches for a specific contact by name."""
    name = input("Enter the name to search for: ").strip()
    if name in contacts:
        print(f"\n🔍 Contact Found:")
        print(f"👤 Name:  {name}")
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"📧 Email: {contacts[name]['email']}")
    else:
        print(f"❌ No contact found matching '{name}'.")

def delete_contact(contacts):
    """Deletes a contact by name."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted successfully.")
    else:
        print(f"❌ Contact '{name}' not found.")

def main():
    """Main execution loop for user interaction."""
    contacts = load_contacts()
    
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit Application")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
