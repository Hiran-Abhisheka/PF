x=[]
count=0
for i in range(1,11):
    y=int(input(f"Number {i}: "))
    x.append(y)
    z=y%2
    if z==0:
        count+=1
print(count)
print(x)