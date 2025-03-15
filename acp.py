start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

for i in range(start, end+1):
sqList = []
even = []
odd = []
 
for i in range(start, end+1):
    square = i ** 2
    sqList.append(i*i)

    if square % 2 == 0:
        even.append(square)
    else: 
        odd.append(square)

print("Square values:", sqList)
print("Even square values:", even)
print("Odd square values:", odd)