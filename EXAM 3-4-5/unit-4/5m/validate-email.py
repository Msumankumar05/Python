import re

def validate_email(email):

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(email_regex, email):
        return True
    return False

# --- Test Cases ---
test_emails = {
    "user.name+tag@example.com": True,
    "hello123_45@subdomain.domain.org": True,
    "invalid-email@domain": False,      # Missing TLD (.com, .org, etc.)
    "://domain.com": False,     # Missing @ symbol
    "user@.com": False,                 # Missing domain name
    "user@domain.c": False,             # TLD too short (must be at least 2 chars)
    "@example.com": False               # Missing username
}

print("📧 Running Email Validation Tests:\n")
for email, expected in test_emails.items():
    is_valid = validate_email(email)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    result_match = "PASS" if is_valid == expected else "FAIL"
    print(f"{email:<35} -> {status:<10} ({result_match})")
