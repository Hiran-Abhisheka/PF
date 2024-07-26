number=list(range(1, 8))

#I
squares = []
for num in number:
    squares.append(pow(num, 2))
print(f"List of squares: {squares}")

#II
for i in range(len(number)):
    number[i] = number[i] ** 2

print("Updated list of numbers with square values:")
print(number)