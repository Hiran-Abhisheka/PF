def celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def print_charts():
    print(f"{'Celsius':<10}{'Fahrenheit':<15} | {'Fahrenheit':<15}{'Celsius'}")
    print("-" * 50)
    for c in range(0, 101, 10):
        f = fahrenheit(c)
        print(f"{c:<10}{f:<15.1f} | ", end="")
        if c * 2 + 32 <= 212:
            f2 = c * 2 + 32
            c2 = celsius(f2)
            print(f"{f2:<15.1f}{c2:.1f}")
        else:
            print("")
print_charts()
