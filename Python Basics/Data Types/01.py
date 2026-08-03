name = "suman"
age = 21
city = "Bangalore"
boolean = True
digit = 10.5
list1 = ["name: John", "age: 21", "city: New York"]

print(list1)

print(f"Hello, {name}! You are {age} years old and live in {city}.")


a, b = 10, 20

a, b = b, a

print(f"after swapping a = {a} and b = {b}")

print(type(name))
print(type(age))
print(type(city))
print(type(boolean))
print(type(digit))
print(type(list1))


x = 10
y = 10

print(x)
print(y)


PI = 3.14
MAX_CONNECTIONS = 100
MAX_CONNECTIONS = 101
print(f"Value of PI: {PI}")
print(f"Max connections allowed: {MAX_CONNECTIONS}")

x = 10
y = x
x = 20

print(x)
print(y)

num = 10 + 20j

print(type(num))

print(10 > 5)

print(20 == 10)

print(5 != 3)



message = """
Hello

Welcome

Python
"""

print(message)


# Duplicate values are removed automatically.

nums = {1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5}

print(nums)

student = {
    "name": "Suman",
    "age": 21,
    "city": "Bangalore"
}

print(student)
print(student["name"])

x = None

print(x)

print(type(x))


age1 = "21"
age2 = int(age1)

print(type(age1))
print(type(age2))

print(age1 + "20")
print((age2) + 20)


numbers = [1,2,3,4,]

numbers.append(50)
print(numbers)