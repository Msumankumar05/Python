class Animal:
    def make_sound(self):
        return "Generic animal sound"

class puppy:
    def make_sound(self):
        return "memu"
class Dog(Animal):
    def make_sound(self):  
        return "Bark!"
class Cat(Animal):
    def make_sound(self):  
        return "Meow!"

a = Animal
print(a.make_sound)

