numbers = []

for i in range(10): 
    num = int(input("Enter number {}: ".format(i+1))) 
    numbers.append(num)

maximum = max(numbers) 
minimum = min(numbers)

print("Maximum number: ", maximum) 
print("Minimum number: ", minimum)