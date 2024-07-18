no=int(input("Enter number: "))
x=no
digit_of_sum=0

while no>0:
    digit=no%10
    digit_of_sum=digit_of_sum+digit
    no=no//10

print(f"Given number: {x}")
print(f"Sum of digits: {digit_of_sum}")