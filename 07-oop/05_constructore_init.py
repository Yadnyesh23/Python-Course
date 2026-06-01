class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order1 = ChaiOrder("Masala", 200)
print(order1.summary())
order2 = ChaiOrder("Lemon", 250)
print(order2.summary())