class Dog:
    # The initializer method
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable

# Creating an object (automatically calls __init__)
my_dog = Dog("Buddy", "Golden Retriever")

print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
