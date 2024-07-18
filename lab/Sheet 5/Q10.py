num=int(input("Enter number: "))
count=0
for i in range(1,num+1):
    rem=num%i
    if rem==0:
        count+=1
if count==2:
    print("It's a prime")
    print("Count: ", count)
else:
    print("Not prime")
    print("Count: ", count)