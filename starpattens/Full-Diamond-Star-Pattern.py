for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(i-(i-1)):
        print("*", end="")
for i in range(5, 1, -1):
    for j in range(5-1):
        print(" ", end="")
    for j in range(i-(i-2)):
        print("*", end="")
    print()
