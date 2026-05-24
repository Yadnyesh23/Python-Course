
# Tasks:

# Create a set branch_a_products with the items: "bread", "milk", "butter", "jam"

# Create another set branch_b_products with the items: "bread", "cheese", "butter", "ketchup"

# Print both sets.

# Find and print the union of both branches’ products.

# Find and print the intersection of both branches’ products.

# Find and print the products that are in branch_a_products but not in branch_b_products.

# Check whether "ketchup" is available in branch_a_products and print the result.

# Define a frozenset called essential_items with values: "milk", "bread", "ketchup".

# Print the frozenset.

branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = { "bread", "cheese", "butter", "ketchup"}

print(f"Branch A Products : {branch_a_products}")
print(f"Branch B Products : {branch_b_products}")

union = branch_a_products | branch_b_products
print(f"Union of both branched : {union}")

intersection = branch_a_products & branch_b_products
print(f"Union of both branched : {intersection}")

only_branch_a = branch_a_products - branch_b_products
print(f"Only branch a : {only_branch_a}")

isKetchupAvail = 'ketchup' in branch_a_products
print(f"Ketchup available in branch_a_products ? : {isKetchupAvail}")