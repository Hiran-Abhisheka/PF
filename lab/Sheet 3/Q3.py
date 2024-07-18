name=str(input("Enter name= "))
sala=float(input("Enter salary= "))

if (sala < 5000):
    increment=sala/100*5
elif(sala >= 5000):
    increment=sala/100*5
elif (sala < 10000):
    increment=sala/100*10
else:
    increment=sala/100*15
Newsalary=sala+increment

print("Ename= ", name)
print("New salary= ",Newsalary)