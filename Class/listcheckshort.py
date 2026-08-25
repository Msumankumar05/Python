a=[]
print("Enter the elements of the list (type 'done' to finish):")

while True:
    element = input("Enter an element (or Type 'done' to finish): ")
    if element == 'done':
        break
    a.append(element)

Asorted = True
Dsorted = True

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        Asorted = False
        break
    else:
        Asorted = True

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        Dsorted = False
        break
    else:
        Dsorted = True

if(Asorted and Dsorted):
    print("The list is sorted in both ascending and descending order.")
elif(Asorted):
    print("The list is sorted in ascending order.")
elif(Dsorted):
    print("The list is sorted in descending order.")
else:
    print("The list is not sorted in either order.")