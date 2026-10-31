class Calculator:
    # Simulating overloading using default arguments
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

# Usage
calc = Calculator()

# Call with 2 arguments
print(calc.add(5, 10))       # Output: 15

# Call with 3 arguments
print(calc.add(5, 10, 20))   # Output: 35


class AuthService:
    # Simulating overloading by setting optional credentials to None
    def login(self, username, password=None, otp=None):
        if password is not None:
            return f"Logging in {username} securely using Password Verification."
        
        elif otp is not None:
            return f"Logging in {username} securely using 6-digit OTP Verification."
        
        else:
            raise ValueError("Invalid login attempt: Provide either a password or an OTP.")

# Usage
auth = AuthService()

# Scenario 1: User logs in with Password
print(auth.login("alice_dev", password="SecurePassword123"))
# Output: Logging in alice_dev securely using Password Verification.

# Scenario 2: User logs in with OTP
print(auth.login("bob_manager", otp=482910))
# Output: Logging in bob_manager securely using 6-digit OTP Verification.
