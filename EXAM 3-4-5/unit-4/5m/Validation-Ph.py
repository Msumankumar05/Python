import re

def validate_indian_mobile(phone_number):
    """
    Validates an Indian mobile number.
    Accepts optional prefixes (+91, 91, 0) and ignores spaces/hyphens.
    Returns True if valid, False otherwise.
    """
    # 1. Clean the input string (remove common dividers like spaces, hyphens, and parentheses)
    clean_number = re.sub(r"[\s\-\(\)]", "", str(phone_number))
    
    # 2. Regex Explanation:
    # ^             : Start of the string
    # (?:\+91|91|0)? : Optional country prefix: "+91", "91", or a single "0"
    # [6-9]         : First digit of the core 10-digit number (must be 6, 7, 8, or 9)
    # \d{9}         : Exactly 9 more digits following the first one
    # $             : End of the string
    mobile_regex = r"^(?:\+91|91|0)?[6-9]\d{9}$"
    
    if re.match(mobile_regex, clean_number):
        return True
    return False

# --- Test Cases ---
test_numbers = {
    "+91 98765 43210": True,   # Standard format with country code and spaces
    "9876543210": True,       # Standard 10-digit format
    "0876543210": True,       # 10-digit format with leading 0
    "917654321098": True,     # 10-digit format with 91 prefix (no plus)
    "+91-63456-78901": True,  # Valid number starting with 6 containing hyphens
    
    "5678901234": False,      # Invalid: Starts with 5 (Landline range)
    "987654321": False,       # Invalid: Only 9 digits long
    "+91 98765 432101": False,# Invalid: 11 digits long
    "98765abcde": False,      # Invalid: Contains non-numeric characters
    "+1 98765 43210": False   # Invalid: Uses a foreign country code (+1)
}

print("📱 Running Indian Mobile Number Validation Tests:\n")
for phone, expected in test_numbers.items():
    is_valid = validate_indian_mobile(phone)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    result_match = "PASS" if is_valid == expected else "FAIL"
    print(f"{phone:<20} -> {status:<10} ({result_match})")
