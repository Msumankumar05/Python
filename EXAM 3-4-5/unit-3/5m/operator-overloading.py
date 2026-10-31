class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def display(self):
        # Format the imaginary part sign gracefully (+ or -)
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {abs(self.imag)}i")


# --- Testing the ComplexNumber Class ---

# Create two complex numbers: (3 + 2i) and (1 + 7i)
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

# 1. Test Addition: (3+1) + (2+7)i = 4 + 9i
result_add = c1 + c2
print("Addition Result:")
result_add.display() 

# 2. Test Multiplication: (3*1 - 2*7) + (3*7 + 2*1)i = -11 + 23i
result_mul = c1 * c2
print("\nMultiplication Result:")
result_mul.display() 
