print("")
print("~~ RESTURANT XYZ LOGIN ~~")

user1 = "Ali"
user2 = "Ahmed"
user3 = "Mia"
password = "HP L"
flag = False
flag2 = False
count = 0
tries = 0

while count != 3:

    while tries != 3:
        Euser = str(input("Enter username: "))

        if (Euser == user1) or (Euser == user2) or (Euser == user3):
            flag = True
            tries = 3
        else:
            print("User undetected.")
            tries = tries + 1

    if (flag == True):
        Epass = str(input("Enter password: "))
        if (Epass == password):
            count = 3
            print("Access granted, Welcome", Euser, ".")
            flag2 = True
        else:
            count = count + 1
            print("Password doest match.")

if (count == 3) and (flag2 == False):
    print("")
    print("Login failed.")
    print("Please wait 15 minutes.")

elif (flag2 == True):
    print("")
    print("~~ MENU ~~")
    print("")
    print("1. Drinks")
    print("2. Fast Food Items")
    print("3. Specialities")
    print("4. Other...")
    print("")

    end = 1
    while end == 1:
        choice = int(input("Pick one option to expand; [1] [2] [3] [4]: "))

        if (choice == 1):
            print("~~ DRINKS ~~")
            print("")
            print("1. Pepsi")
            print("2. CocaCola")
            print("3. Sprite")
            print("4. Cola Next")
            print("")

        elif (choice == 2):
            print("~~ FAST FOOD ITEMS ~~")
            print("")
            print("1. Burger")
            print("2. CocaCola")
            print("3. Sprite")
            print("4. Cola Next")
            print("")
            end = int(input("Do you want to end program? [1 for NO] [0 for YES]: "))

        elif (choice == 3):
            print("~~ SPECIALITIES ~~")
            print("")
            print("1. Corn Soup")
            print("2. Steak")
            print("3. Chicken Fillet")
            print("4. Salad")
            print("")
            end = int(input("Do you want to end program? [1 for NO] [0 for YES]: "))

        elif (choice == 4):
            print("~~ OTHER ~~")
            print("")
            print("1. Chocolate Cake")
            print("2. Ice Cream Cake")
            print("3. Ice Cream")
            print("4. Sundae")
            print("")
            end = int(input("Do you want to end program? [1 for NO] [0 for YES]: "))

        # Function definitions
        def add(drinks, foods):
            total = drinks + foods
            return total

        choice = 2

        if choice == 2:
            d = int(input("Enter the drinks price: "))
            f = int(input("Enter the foods price: "))
            print("Result is:", add(d, f))
            end = int(input("Do you want to end program? [1 for NO] [0 for YES]: "))

    
