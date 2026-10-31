import re

odd_words = []
even_count = 0


with open("input.txt", "r") as infile, open("odd_words.txt", "w") as outfile:
    text = infile.read()
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    
    for word in words:
        if len(word) % 2 != 0:
            odd_words.append(word)
        else:
            even_count += 1
            
    outfile.write(" ".join(odd_words))

print("Odd-length words:", len(odd_words))
print("Even-length words:", even_count)
print("Odd words written to odd_words.txt")
