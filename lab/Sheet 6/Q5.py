'''item1="Apple"
item2="Orange"
item3="Mango"

amount1=2.3
amount2="3"
amount3=5

price1="5.99"
price2=3.50
price3=2

'''
# Sample input data
item1 = "Apple"
amount1 = 2.3
price1 = "5.99"
item2 = "Orange"
amount2 = "3"
price2 = 3.50
item3 = "Mango"
amount3 = 5
price3 = 2

# Convert input data to appropriate types
amount1 = float(amount1)
price1 = float(price1)
amount2 = int(amount2)
price2 = float(price2)

# Calculate total number of items
total_items = amount1 + amount2 + amount3

# Calculate total price
total_price = price1 * amount1 + price2 * amount2 + price3

# Display results
print(f"Total number of items: {total_items}")
print(f"Total price: ${total_price:.2f}")
