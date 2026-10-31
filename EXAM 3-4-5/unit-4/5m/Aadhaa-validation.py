import re

def validate_aadhaar(uid):
    # 1. Clean and validate shape (12 digits, must start with 2-9)
    clean = re.sub(r"[\s-]", "", str(uid))
    if not re.match(r"^[2-9]\d{11}$", clean): 
        return False
        
    # 2. Inline Verhoeff Checksum calculation
    d = [[(i + j) % 5 if i < 5 and j < 5 else (i + j - 5) % 5 + 5 if i >= 5 and j >= 5 else (i + (5 - j)) % 5 if i < 5 else (i + (5 - j) - 5) % 5 + 5 for j in range(10)] for i in range(10)]
    p = [[0,1,2,3,4,5,6,7,8,9], [1,5,7,6,2,8,3,0,9,4], [5,8,0,3,7,9,6,1,4,2], [8,9,1,6,0,4,3,5,2,7], [9,4,5,3,1,2,6,8,7,0], [4,2,8,6,5,7,3,9,0,1], [2,7,9,3,8,0,6,4,1,5], [7,0,4,6,9,1,3,5,8,2]]
    
    checksum = 0
    for i, num in enumerate(reversed([int(x) for x in clean])):
        checksum = d[checksum][p[i % 8][num]]
        
    return checksum == 0

# --- Quick Test ---
for uid in ["3675 9834 6012", "3675 9834 6013", "012345678912"]:
    print(f"{uid:<16} -> {'✅ Valid' if validate_aadhaar(uid) else '❌ Invalid'}")
