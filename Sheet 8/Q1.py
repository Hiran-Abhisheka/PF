def cal():
    num1=int(input("Enter base number: "))
    num2=int(input("Enter exponent number: "))
    if num2==0:
        print("answer is: 1")
    else:
        c=num1**num2
        print(f"answer is:{c}")
cal()