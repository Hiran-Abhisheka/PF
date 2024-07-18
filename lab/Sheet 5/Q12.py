total=0
x=1
while(x>=1):
    i=int(input("Enter number(-1 to end): "))
    total=total+i
    if(i==-1):
        print("Total: ",total+1)
        break