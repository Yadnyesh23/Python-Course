class Chai:
    origin = "India"
    
print(Chai.origin)

Chai.is_hot = True
print(Chai.origin)
print(Chai.is_hot)

masala_tea = Chai()
print(f"Masala : {masala_tea.origin}")
print(f"Masala : {masala_tea.is_hot}")

masala_tea.is_hot = False

print(f"Masala : {masala_tea.is_hot}")


# Mobile example
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
mobile1 = Mobile("Samsung", "S25", 80000)
mobile2 = Mobile("Apple", "iPhone 17", 120000)

print(f"Mobile 1 data : \n Brand :{mobile1.brand} \n Model : {mobile1.model} \n Price : {mobile1.price}")
print(f"Mobile 2 data : \n Brand :{mobile2.brand} \n Model : {mobile2.model} \n Price : {mobile2.price}")

print(mobile1.__dict__)
print(type(mobile1.__dict__))
print(mobile2.__dict__)
print(type(mobile2.__dict__))