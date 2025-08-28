def menu():
    items = []
    while True:
        print("\n--- MENU ---")
        print("1. Add")
        print("2. Delete")
        print("3. Show All")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            item1 = input("Enter item to add: ")
            priceIt1 = input("Enter Price: ")
            items.append((item1, priceIt1))   # ✅ append tuple
            print(f"Item '{item1}' with price {priceIt1} added.")

        elif choice == "2":
            item2 = input("Enter item to delete: ")
            found = False
            for i in items:
                if i[0] == item2:   # ✅ match by item name
                    items.remove(i)
                    print(f"'{item2}' deleted successfully.")
                    found = True
                    break
            if not found:
                print("Item not found.")

        elif choice == "3":
            if items:
                print("\nItems are:")
                for i, (name, price) in enumerate(items, start=1):
                    print(f"{i}. {name} - {price}")
            else:
                print("No items in the list.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter between 1-4.")


# Run the menu
menu()
