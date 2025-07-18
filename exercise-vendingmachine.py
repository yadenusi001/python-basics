
# vending machine menu items
items = {
    "soda": 1.50,
    "chips": 2.00,
    "candy": 1.00
}


# Add funds to vending machine
funds = float(input("Welcome! How much money would you like to insert? $"))

# Display menu function
def display_menu():
    print("\nAvailable items:")
    for item, price in items.items():
        print(f"- {item.capitalize()}: ${price:.2f}")

# Transaction loop
while funds > 0:
    display_menu()
    print(f"\nCurrent balance: ${funds:.2f}")
    choice = input("Please select an item by name: ").lower()

    # Check if item exists
    if choice not in items:
        print("Sorry, that item is not available. Please choose again.")
        continue

    item_price = items[choice]

    # Check if user has enough funds
    if funds >= item_price:
        funds -= item_price
        purchased_items.append(choice)
        print(f"Dispensing {choice}. Enjoy!")
        print(f"Remaining balance: ${funds:.2f}")
    else:
        print(f"Insufficient funds for {choice}. It costs ${item_price:.2f} but you only have ${funds:.2f}.")
        add_more = input("Would you like to insert more money? (yes/no): ").lower()
        if add_more == "yes":
            additional = float(input("How much more money would you like to insert? $"))
            funds += additional
            print(f"New balance: ${funds:.2f}")
            continue
        else:
            print("Transaction canceled.")
            break

    # Ask if user wants to buy more
    more = input("Would you like to buy another item? (yes/no): ").lower()
    if more != "yes":
        break

# Final summary
print("\nThank you for using the vending machine!")
if purchased_items:
    print("You purchased the following items:")
    for item in purchased_items:
        print(f"- {item.capitalize()}")
    total_spent = sum(items[item] for item in purchased_items)
    print(f"Total spent: ${total_spent:.2f}")
else:
    print("You did not purchase any items.")
print(f"Remaining balance returned: ${funds:.2f}")