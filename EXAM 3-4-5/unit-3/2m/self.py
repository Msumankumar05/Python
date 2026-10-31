class Dog:
    # Constructor method to initialize attributes for each object
    def __init__(self, name, breed):
        self.name = name    # Attaching 'name' to the specific object
        self.breed = breed  # Attaching 'breed' to the specific object

    # Instance method using self to access the object's data
    def bark(self):
        print(f"{self.name} the {self.breed} says woof!")


# Creating two distinct objects from the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")

# Calling the method on each object
dog1.bark()  # Output: Buddy the Golden Retriever says woof!
dog2.bark()  # Output: Lucy the Beagle says woof!
