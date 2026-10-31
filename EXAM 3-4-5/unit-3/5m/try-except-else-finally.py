def divide_numbers(a, b):
    try:
        print("\n--- Starting Calculation ---")
        result = a / b
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    else:
        print(f"Success! The answer is: {result}")
    finally:
        print("Cleaning up... Calculation process finished.")

# Testing the safe path
divide_numbers(10, 0)
