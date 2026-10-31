class product:
    def input(self):
        self.no = int(input("Enter product no: "))
        self.Name = input("Enter product name: ")
        self.cost = float(input("Enter product cost: "))
        self.quantity = int(input("Enter product quantity: "))

    def calculate(self):
        self.totalamount = self.cost * self.quantity

    def display(self):
        print(self.no, self.Name,
              self.cost, self.quantity, self.totalamount)

products = []

for i in range(2):
    p = product()
    p.input()
    p.calculate()
    p.display()

    products.append(p)

highest = max(products, key=lambda p: p.totalamount)

print("Product with highest total cost:")
highest.display()