while True:
    x=float(input("Enter first number: "))
    y=float(input("Enter second number: "))
    z=float(input("Enter third number: "))

    def num(x, y, z):
        return min(x, y, z)
    smallest= num(x, y, z)
    print(f"Smallest number is: {smallest}")