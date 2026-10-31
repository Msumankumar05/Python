class Base:
    pass

class A(Base):
    def greet(self):
        print("Hello from A")

class B(Base):
    def greet(self):
        print("Hello from B")

# Multiple inheritance: Python evaluates A first, then B
class Child(A, B):
    pass

# Displaying the MRO
print("Using .mro():", Child.mro())

