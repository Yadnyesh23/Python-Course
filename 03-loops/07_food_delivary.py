# Food Delivery Order Tracker

# Imagine you are building a backend feature for a food delivery app.

# Customers place multiple food orders, and the restaurant has limited stock available.

# Use a while loop to iterate through the list named orders.

# For every order:

# ✅ If enough stock is available:

# Reduce the stock
# Append: "Order served: {quantity}"

# ❌ If stock is not enough:

# Append:
# "Not enough stock for order: {quantity}"

# After processing all orders:

# Append:
# "Remaining Stock: {stock}"

# Return all messages inside a list.

orders = [3, 2, 12, 4]
stock = 10
messages = []

i = 0
while i < len(orders):
    if orders[i] <= stock:
         stock -= orders[i]
         messages.append(f"Order served: {orders[i]}")
    else : 
        messages.append(f"Not enough stock for order: {orders[i]}")
        
    i += 1
    
messages.append(f"Remaining Stock: {stock}")

for num, msg in enumerate(messages, start=1):
    print(num, msg)