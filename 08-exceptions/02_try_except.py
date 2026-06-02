orders = {"Masala Chai" : 300, "Ginger Chai" : 250}

try:
    print(orders["Elaichi Chai"])
except KeyError:
    print("The key u r trying to acces is not present")