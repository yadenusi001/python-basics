#play with for loops

# create a list
shopping_cart = []
print("Your shopping cart:",)

# Add items to the cart
shopping_cart.append("Milk")
shopping_cart.append("Bread")
shopping_cart.append("Eggs")

print("Updated cart:",)

# Insert an item 
shopping_cart.insert(1, "Butter")
print("After inserting an item:", )

# Remove an item after purchase
purchased_item = shopping_cart.pop(2)
print("You purchased:", purchased_item)
print("Cart after removing purchased item:",)

print("Here’s what’s still in your cart:")
for item in shopping_cart:
    print("-", item)