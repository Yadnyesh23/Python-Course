# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# Step 2: Add email and phone
customer.update({
    "email": "john@gmail.com",
    "phone": 9867637173
})

print(customer)

# Step 3: Print customer's name and city
name = customer['name']
city = customer['city']

print(f"City : {city} , Name : {name}")

# Step 4: Check if "email" exists
print(f"Email : {customer.get('email')}")

# Step 5: Delete the "age" field
del customer["age"]

print(customer)

# Step 6: Print all keys, values, and items
print(f"All Keys : {customer.keys()}")
print(f"All values : {customer.values()}")
print(f"All items : {customer.items()}")

# Step 7: Remove and print the last inserted item
last_item = customer.popitem()

print(last_item)

# Step 8: Use .get() to access "membership"
membership = customer.get("membership")

print(f"Membership : {membership}")

# Step 9: Update dictionary with "address"
customer["address"] = "221B Baker Street"

# Step 10: Print final dictionary
print(customer)