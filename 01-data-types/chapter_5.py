# Create a grocery list
my_cart = ["apples", "bananas", "milk"]

# Print the grocery list
print("Initial list:", my_cart)

# Add "bread" to the end of the list
my_cart.append("bread")

# Print the updated grocery list
print("After adding bread:", my_cart)

# Insert "ketchup" at the beginning of the list
my_cart.insert(0, "ketchup")

# Print the updated grocery list
print("After inserting ketchup:", my_cart)

# Remove "bananas" from the list
my_cart.remove("bananas")

# Print the updated grocery list
print("After removing bananas:", my_cart)

# Remove the last item and store it in removed_item
removed_item = my_cart.pop()

# Print the value of removed_item
print("Removed item:", removed_item)

# Extend the grocery list
my_cart.extend(["rice", "butter"])

# Print the updated grocery list
print("After extending list:", my_cart)

# Sort the grocery list alphabetically
my_cart.sort()

# Print the updated grocery list
print("After sorting:", my_cart)

# Reverse the order of the grocery list
my_cart.reverse()

# Print the updated grocery list
print("After reversing:", my_cart)

# Concatenate with another list
new_list = my_cart + ["juice", "jam"]

# Print the resulting list
print("After concatenation:", new_list)

# Duplicate the grocery list twice
duplicated_list = my_cart * 2

# Print the resulting list
print("Duplicated list:", duplicated_list)

# Convert string into a list
vegetables = "tomato cucumber spinach"
vegetable_list = vegetables.split()

# Print the converted list
print("Converted vegetable list:", vegetable_list)