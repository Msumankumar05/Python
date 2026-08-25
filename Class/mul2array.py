a=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=int(input(f"Enter the value of a[{i}][{j}]: "))

for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j]=int(input(f"Enter the value of b[{i}][{j}]: "))

print("\n")
print("Matrix A:")
for row in a:
    print(row)

print("\n")
print("Matrix B:")
for row in b:
    print(row)
print("\n")

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=a[i][j]*b[j][i]

print("After multiplication of two matrices:")

for row in a:
    print(row)