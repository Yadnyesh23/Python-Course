# Inheritance
#Parent class
class BaseChai:
    
    def __init__(self, type_):
        self.type = type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai....")
       
# Child class
class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding cardomom, ginger, clove")
        
# Composition
class ChaiShop:
    chai_cls=BaseChai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in shop.")
        self.chai.prepare()
    
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
    
shop = ChaiShop()
fanchishop = FancyChaiShop()