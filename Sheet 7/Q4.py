number1=int(input("Enter First number: "))
number2=int(input("Enter second number: "))

def calculate_quotient(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    quotient = num1 // num2
    return quotient
result = calculate_quotient(number1, number2)
print(f"The quotient of {number1} divided by {number2} is: {result}")
