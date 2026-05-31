# Smart Inventory Filter
# You are building a Smart Inventory Filter for a retail store.

# Tasks:

# Process a list of product dictionaries, where each product has name, price, and category.

# Use different types of comprehensions to:

# Extract names of products priced below ₹5000 using list comprehension.

# Extract all unique categories using set comprehension.

# Create a name-to-price mapping using dictionary comprehension.

# Generate a list of discounted prices using a generator expression and convert it to a list.

# Return all four outputs as a tuple.

products = [
    {"name": "Laptop", "price": 65000, "category": "Electronics"},
    {"name": "Running Shoes", "price": 3500, "category": "Footwear"},
    {"name": "Water Bottle", "price": 500, "category": "Accessories"},
    {"name": "Backpack", "price": 1800, "category": "Bags"},
    {"name": "Wireless Mouse", "price": 1200, "category": "Electronics"}
]

# List Comprehension
# Extract names of products priced below ₹500 using list comprehension.
products_below_5000 = [product for product in products if product['price'] < 5000 ]
print(products_below_5000)


# Set Comprehension
# Extract all unique categories using set comprehension.
unique_categories = {product["category"] for product in products}
print(f"Unique Product categories : {unique_categories}")

# Dictionary Comprehension
# Create a name-to-price mapping using dictionary comprehension.
name_to_price = {product["name"]:product["price"] for product in products}
print(f"Name to price : {name_to_price}")

# Generator Comprehension
# Generate a list of discounted prices using a generator expression and convert it to a list.
discounted_products = list(product["price"] * 0.9 for product in products)
print(f"Discounted Prices : {discounted_products}")