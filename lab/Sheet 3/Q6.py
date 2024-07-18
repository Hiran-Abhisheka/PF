monthlysales=float(input("Enter monthly sales: "))
basicsalary=float(input("Enter basic salary: "))
service=int(input("Enter service year: "))
city=input("Enter city: ")

if service>5:
    allowance=basicsalary*10/100
else:
    allowance=0

if (city=='c'):
    allowance=allowance+2500

if monthlysales<25000:
    bonus=10
elif 25000<=monthlysales<50000:
    bonus=12
else:
    bonus=15

bonus=(bonus/100*monthlysales)
remuration=basicsalary+allowance+bonus

print("Remuration is ", remuration )
print("Bonus is ", bonus)
print("Alloence is ", allowance)