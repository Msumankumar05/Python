class StandardShipping:
    def calculate_cost(self, weight):
        return weight * 50  # ₹50 per kg

class PremiumShipping(StandardShipping):
    # Overriding to add an express handling fee
    def calculate_cost(self, weight):
        base_cost = super().calculate_cost(weight)
        return base_cost + 200  # Base cost + ₹200 express fee

# Usage
standard = StandardShipping()
premium = PremiumShipping()

print(f"Standard Shipping: ₹{standard.calculate_cost(10)}")  # Output: ₹500
print(f"Premium Shipping:  ₹{premium.calculate_cost(10)}")   # Output: ₹700
