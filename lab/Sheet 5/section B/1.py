pos_count = 0
neg_count = 0
zero_count = 0
count=0
for i in range(10):
    num = float(input("Enter a number: "))
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1

print("Positive numbers in the list:", pos_count)
print("Negative numbers in the list:", neg_count)
print("Zero numbers in the list:", zero_count)