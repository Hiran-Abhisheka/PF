import math
number = 0.6523
rounded_down = math.floor(number)
rounded = round(number)
print(f"The result of rounding down {number} using math.floor is: {rounded_down}")
print(f"The result of rounding {number} using round() is: {rounded}")
explanation = """
The math.floor function rounds the number down to the nearest whole number, regardless of its decimal value.
In contrast, the round() function rounds the number to the nearest whole number. If the fractional component
of the number is 0.5 or greater, round() rounds up. Otherwise, it rounds down.
"""
print(explanation)
