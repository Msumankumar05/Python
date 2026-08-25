# n = input("enter a string to check wheater is palindrome or not : ")

# x = 0
# y = len(n) -1

# isPali = True

# while x < y:
#     if n[x] != n[y]:
#         isPali = False
#         break 
#     x+=1
#     y-=1

# if isPali:
#     print("the enter string is a palindrome")
# else:
#     print("the enter string is not a palindrome")



# print("Counting the number of vowels in a string")


# text = input("enter a number to check vowels count : ")

# vowels = "aeiouAEIOU"
# count = 1


# for  char in text:
#     if text in vowels:
#         count += 1

# print(count)



# print("Removing the Spacing in input string")

# text = input("Enter a string with space : ")

# result = text.replace(" ","")

# print(result)


print("Printing the word using a loop ")

text = input("enter a string").replace(" ","")

for i in text:
    print(i)