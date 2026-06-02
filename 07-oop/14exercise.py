# You are designing a Vehicle Rental System that tracks different types of vehicles and their components.


# Tasks:

# Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".

# Create class Vehicle

# Attributes: brand, model, and an Engine object.

# Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).

# Add a method get_details() returning brand, model, and engine info.

# Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".

# Add @classmethod get_total_vehicles() → returns total number of vehicles.

# Add a @property rental_price and corresponding setter that ensures the value is non-negative.-

# Create a Car class that inherits from Vehicle.

# Add an attribute seats.

# Override the get_details() method and use super() to include base details and append "Seats: X".

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, engine, rental_price=0):
        self.brand = brand
        self.model = model
        self.engine = engine
        self._rental_price = rental_price

        Vehicle.total_vehicles += 1

    def get_details(self):
        return (
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"Engine: {self.engine.get_engine_info()}"
        )

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value < 0:
            raise ValueError("Rental price cannot be negative")
        self._rental_price = value


class Car(Vehicle):
    def __init__(self, brand, model, engine, seats, rental_price=0):
        super().__init__(brand, model, engine, rental_price)
        self.seats = seats

    def get_details(self):
        return f"{super().get_details()}\nSeats: {self.seats}"
    
engine1 = Engine(150)

car1 = Car("Toyota", "Camry", engine1, 5, 1000)
car2 = Car("Honda", "City", engine1, 5, 1200)

print(car1.get_details())

print("\nVehicle Type:")
print(Vehicle.get_vehicle_type())

print("\nTotal Vehicles:")
print(Vehicle.get_total_vehicles())

print("\nRental Price:")
print(car1.rental_price)