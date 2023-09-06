print("Please select from the following items")
print("Item 1 : Chips - 50")
print("Item 2 : Biscuits - 20")
print("Item 3 : Coke - 60")
print("Item 4 : Chocolate - 100")
print("Item 5 : Coffee - 70")

while True:
    item = int(input("Enter item number to purchase: "))
    quantity = int(input("Enter quantity: "))

    if item == 1:
        price = 50 * quantity
        print(f"Your total price is {price}")
    elif item == 2:
        price = 20 * quantity
        print(f"Your total price is {price}")
    elif item == 3:
        price = 60 * quantity
        print(f"Your total price is {price}")
    elif item == 4:
        price = 100 * quantity
        print(f"Your total price is {price}")
    elif item == 5:
        price = 70 * quantity
        print(f"Your total price is {price}")
    else:
        print("Invalid item number. Please choose a valid item.")

    input_val = int(
        input("\nDo you want to shop more?\nPress 1 for yes and 0 to dismiss: "))

    if input_val == 0:
        print("Thank you for Shopping")
        break
    elif input_val != 1:
        print("Invalid input. Please enter 1 to continue shopping or 0 to dismiss.")
