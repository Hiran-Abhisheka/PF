print("Select Operator\n"
"1= Addition (+) \n"
"2= Substraction (-)\n"
"3= Divition (/)\n"
"4= Multi (*)")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
choice=int(input("Enter your operator number: "))

if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    if num2==0:
        print("Error")
    else:
        print(num1/num2)
elif choice==4:
    print(num1*num2)
else:
    print("Invalid Operator")