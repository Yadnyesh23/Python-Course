# You’re creating a menu price lookup system for a digital food 
# ordering app using the match-case statement.

# Tasks:

# Define a function get_item_price that takes a string input item.

# Use match-case to return the following based on the item name:

# "pizza" → "Price: 30 bucks"

# "burger" → "Price: 15 bucks"

# "pasta" → "Price: 20 bucks"

# "salad" → "Price: 10 bucks"

# Any other item → "Item not available"

# Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).

item = input("Enter the item name : ").lower()

match item :
    case "pizza" :
        print("Price: 30 bucks")
    case "burger" :
        print("Price: 15 bucks")
    case "pasta" :
        print("Price: 20 bucks")
    case _:
        print("Item not available")