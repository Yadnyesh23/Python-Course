# def serve_chai():
#     yield "Cup 1 : Masala Chai"
#     yield "Cup 2 : Ginger Tea"
#     yield "Cup 3 : Lemon Tea"
    
# stall = serve_chai()

def get_chai_gen() :
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
    
chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))


def chai_customer() :
    print("Welcome! What chai would you like ? ")
    order = yield
    while True:
        print(f"Preparing : {order}")
        order = yield
        
stall = chai_customer()
next(stall)


def local_chai() :
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai() :
    yield "Matcha"
    yield "Oolong"
    
def full_menu() :
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)