#types of creating Stirings in python


# single quotes

name = 'suman'


# double quotes

city = "delhi"



#using triple quotes

message = """
Hello everyone,
My name is suman and I live in delhi.
I am learning python programming.
"""

# for i in range(len(message)):
#     if message[i] == " " or message[i] == "\n" or message[i] == "\t":
#         continue
#     print(message[i])

print(city[::1])
print(city[::2])  # slicing of string

print(len(city))  # length of string
print(len(message))  # length of string


print(name.upper())  # convert to uppercase

print(name.lower())  # convert to lowercase

print(name  * 3)  # repeat string 3 times

print(message.strip())  # remove leading and trailing whitespace


print(message.replace("suman", "John"))  # replace substring

print(name.count("a"))  # count occurrences of substring