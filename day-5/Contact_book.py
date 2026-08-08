contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added!")
    
    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    
    elif choice == "4":
        break
    
    else:
        print("Invalid choice!")
        