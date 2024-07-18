count=0
items=[]
for i in range(1, 11):
    item=int(input(f"Enter the price of an item {i}: "))
    items.append(item)
    if item<=200:
        count+=1
    else:
        EncodingWarning
avg_mark = sum(items) / len(items)
print("Avg: ",avg_mark)
print("Above 200: ", count)
