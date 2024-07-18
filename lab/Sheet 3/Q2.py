num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
smallest = num1
largest = num1
if num2 < smallest:
    smallest = num2
if num2 > largest:
    largest = num2
if num3 < smallest:
    smallest = num3
if num3 > largest:
    largest = num3
print("The smallest number is:", smallest)
print("The largest number is:", largest)