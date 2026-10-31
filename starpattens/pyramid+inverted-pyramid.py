for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i-1):
        print("*", end="")
    print()
for i in range(5, 1, -1):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i-1):
        print("*", end="")
    for j in range(i-2):
        print("*", end="")
    print()