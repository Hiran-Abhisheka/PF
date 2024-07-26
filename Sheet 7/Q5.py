def cal():
    number1=int(input("Enter First number: "))
    number2=int(input("Enter second number: "))
    c=number1+number2
    print(f"Sum of two numbers is: {c}")
def main_loop():
    while True:
        cal()
if __name__ == "__main__":
    main_loop()