class Car:
    def __init__(self, brand, model):
        # Instance variables unique to each object
        self.brand = brand
        self.model = model
        self.odometer = 0

    # Instance method that reads attributes
    def display_info(self):
        return f"{self.brand} {self.model} with {self.odometer} miles."

    # Instance method that modifies attributes and accepts extra arguments
    def drive(self, miles):
        self.odometer += miles
        print(f"Drove {miles} miles!")


# 1. Create an instance (object) of the Car class
my_car = Car("Toyota", "Corolla")

# 2. Call an instance method that returns a value
print(my_car.display_info())
# Output: Toyota Corolla with 0 miles.

# 3. Call an instance method that modifies the object's data
my_car.drive(150)
# Output: Drove 150 miles!

# 4. Read the updated info
print(my_car.display_info())
# Output: Toyota Corolla with 150 miles.
