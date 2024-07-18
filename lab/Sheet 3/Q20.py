num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
num3=int(input("Enter num 3: "))
max=num1
if num2>max:
    max=num2
if num3>max:
    max=num3
min=num1
if num2<min:
    min=num2
if num3<min:
    min=num3
print("The highest num is ", max)
print("The lowest num is ", min)