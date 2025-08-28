print("")
print("~~ RESTAURANT XYZ LOGIN ~~")

# Users and password
users = ["Ali", "Ahmed", "Mia"]
password = "HP L"

flag = False
flag2 = False
count = 0
tries = 0

# Login system
while count != 3:
    while tries != 3:
        Euser = input("Enter username: ")
        if Euser in users:
            flag = True
            tries = 3
        else:
            print("User undetected.")
            tries += 1

    if flag:
        Epass = input("Enter password: ")
        if Epass == password:
            count = 3
            print("Access granted, Welcome", Euser, ".")
            flag2 = True
        else:
            count += 1
            print("Password does not match.")

if (count == 3) and (flag2 == False):
    print("\nLogin failed.")
    print("Please wait 15 minutes.")

elif flag2:
    # Easy add and delete functions
    def add(drinks, foods):
        return drinks + foods

    def delete_item(name, items):
        if name in items:
            items.remove(name)
            print(name, "has been deleted")
        else:
            print(name, "not found")
        return items

    # Menu categories
    menu = {
        1: ["Pepsi", "CocaCola", "Sprite", "Cola Next"],
        2: ["Burger", "Sandwich", "Fries", "Pizza"],
        3: ["Corn Soup", "Steak", "Chicken Fillet", "Salad"],
        4: ["Chocolate Cake", "Ice Cream Cake", "Ice Cream", "Sundae"]
    }

    print("\n~~ MENU ~~")
    print("1. Drinks\n2. Fast Food\n3. Specialities\n4. Other\n")

    end = 1
    while end == 1:
        choice = int(input("Pick one option [1-4]: "))
        if choice in menu:
            print("\nItems:", menu[choice])

            action = input("Do you want to [add] prices or [delete] an item? ")

            if action.lower() == "delete":
                item = input("Enter item name to delete: ")
                menu[choice] = delete_item(item, menu[choice])
                print("Updated list:", menu[choice])

            elif action.lower() == "add":
                d = int(input("Enter the drinks price: "))
                f = int(input("Enter the foods price: "))
                print("Total is:", add(d, f))

        end = int(input("\nDo you want to continue? [1=YES] [0=NO]: "))
