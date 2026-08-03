a = [[0, 0], [0, 0], [0, 0]]
b = [[0, 0], [0, 0], [0, 0]]
x = [[0, 0], [0, 0], [0, 0]]
y = [[0, 0], [0, 0], [0, 0]]


for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(input(f"Enter value for a[{i}][{j}]: "))

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(input(f"Enter value for b[{i}][{j}]: "))

print("Array a:")
for row in a:
    print(row)

print("Array b:")
for row in b:
    print(row)


for i in range(len(a)):
    for j in range(len(a[i])):
        x[i][j] = a[i][j] + b[i][j]


print("Array x after addition:")
for row in x:
    print(row)


for i in range(len(a)):
    for j in range(len(a[i])):
        y[i][j] = a[i][j] * b[i][j]


print("Array y after multiplication:")
for row in y:
    print(row)