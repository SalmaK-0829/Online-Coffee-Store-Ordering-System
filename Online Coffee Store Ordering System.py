# welcome customer

print("Welcome to our coffee store")
# customer data

Name = input("Please enter your name: ")
Address = input("Please enter your address: ")
phone_number = int(input("Please enter your number: "))

# disply menu
def disply_menu():
    print("1.Coffee menu")
    print("2.Desert menu")
    print("3.Sandwiches menu")
    print("4.Show order")
    print("5.Receipt")
    print("6.Quit")

def Get_Menu_Option():
    option=int(input("chose a number from 1 to 6: "))
    return option

# Order details
def order_details(order):
    print("Your current order:")
    for item in order:
        print(item)

# Receipt
def generate_receipt(order, total):
    print("----- Receipt -----")
    print("Your order:")
    for item in order:
        print(item)
    print(f"Total: {total} EGP")
    print("-------------------")

# coffee menu

def coffee_menu():
    print("1.Espresso", "price:35")
    print("2.Cold berw", "price:85")
    print("3.Latte", "price:75")
    print("4.Cappuccino", "price:65")
    print("5.Mocha", "price:90")
    print("6. Quit")
def Get_Coffee_Option():
    option=int(input("chose a number from 1 to 6: "))
    return option

def Execute_Coffee_Options(order):
    while True:
        coffee_menu()
        choice=Get_Coffee_Option()
        
        if choice == 1:
            order.append("Espresso")
        elif choice == 2:
            order.append("Cold Brew")
        elif choice == 3:
            order.append("latte")
        elif choice == 4:
            order.append("Cappuccino")
        elif choice == 5:
            order.append("mocha")
        elif choice == 6:
            break
        else:
            print("not valid,choose number from 1 to 6")


# desert menu

def dessert_menu():
    print("1.Chocolate cake", "price:60")
    print("2.Honey cake", "price:50")
    print("3.Brownies", "price:40")
    print("4.Cookies", "price:40")
    print("5.Muffin", "price:50")
    print("6. Quit")

def Get_Dessert_Option():
    option=int(input("chose a number from 1 to 6: "))
    return option

def Execute_Dessert_Options(order):
    while True:
        dessert_menu()
        choice=Get_Dessert_Option()
        
        if choice == 1:
            order.append("Chocolate cake")
        elif choice == 2:
            order.append("Honey cake")
        elif choice == 3:
            order.append("Brownies")
        elif choice==4:
            order.append("Cookies")
        elif choice==5:
            order.append("Muffin")
        elif choice == 6:
            break
        else:
            print("not valid,choose number from 1 to 6")

# sandwiches menu

def sandwiches_menu():
    print("1.Turkey sandwich", "price:115")
    print("2.Smoked salmon sandwich", "price:160")
    print("3.Triple cheese sandwich", "price:110")
    print("4.Tuna sandwich", "price:130")
    print("5.Club sandwich", "price:115")
    print("6. Quit")

def Get_Sandwiches_Option():
    option=int(input("chose a number from 1 to 6: "))
    return option

def Execute_Sandwiches_Options(order):
    while True:
        sandwiches_menu()
        choice=Get_Sandwiches_Option()
        
        if choice == 1:
            order.append("Turkey sandwich")
        elif choice == 2:
            order.append("Smoked salmon sandwich")
        elif choice == 3:
            order.append("Triple cheese sandwich")
        elif choice == 4:
            order.append("Tuna sandwich")
        elif choice == 5:
            order.append("Club sandwich")
        elif choice == 6:
            break
        else:
            print("not valid,choose number from 1 to 6")
# Initialize order list
order = []

def Execute_Menu_Options():
    while True:
        disply_menu()
        choice=Get_Menu_Option()
        
        if choice==1:
            Execute_Coffee_Options(order)
        elif choice==2:
            Execute_Dessert_Options(order)
        elif choice==3:
            Execute_Sandwiches_Options(order)
        elif choice==4:
            order_details(order)
        elif choice==5:
            generate_receipt(order, calculate_total(order))
        elif choice==6:
            print("Thanks for your order: Have a nice day")
            break
        else:
            print("not valid,choose number from 1 to 6")

def calculate_total(order):
    prices = {
        "Espresso": 35,
        "Cold Brew": 85,
        "Latte": 75,
        "Cappuccino": 65,
        "Mocha": 90,
        "Chocolate cake": 60,
        "Honey cake": 50,
        "Brownies": 40,
        "Cookies": 40,
        "Muffin": 50,
        "Turkey sandwich": 115,
        "Smoked salmon sandwich": 160,
        "Triple cheese sandwich": 110,
        "Tuna sandwich": 130,
        "Club sandwich": 115,
    }

    total_cost = sum(prices[item] for item in order if item in prices)
    return total_cost



# Start the ordering system
Execute_Menu_Options()