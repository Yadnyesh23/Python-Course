# You’re building a delivery system for an e-commerce platform.
# Depending on the distance of the customer’s address,
# different delivery charges apply.

# Tasks:
# Take input from the user for delivery distance in Kilometers and store it in a variable named distance.
# If the distance is 2 km or less, return the string: "Delivery charge: 0"
# If the distance is greater than 2 km but not more than 5 km, return the string: "Delivery charge: 30"
# If the distance is greater than 5 km but not more than 10 km, return the string: "Delivery charge: 50"
# If the distance is more than 10 km, return the string: "Delivery not available for your location."

distance = int(input("Enter the distance (in Kms) : "))

if distance <= 2:
    print("Delivery charge: 0")

elif distance <= 5:
    print("Delivery charge: 30")

elif distance <= 10:
    print("Delivery charge: 50")

else:
    print("Delivery not available for your location.")