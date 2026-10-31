import re

with open("products.py", "r") as file:
        text = file.read().lower()
        words = re.findall(r"\b[a-z]+\b", text)


palindromes = [word for word in words if word == word[::-1]]

print("Palindrome words:", palindromes)
print("Total palindrome words:", len(palindromes))