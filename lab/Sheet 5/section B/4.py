count=0
while True:
    x=int(input("Enter employee NO: "))
    if x==-999:
        break
    y=int(input("Enter employee basic salary: "))
    if y>=5000:
        count+=1
print(f"The number of employees with Basic Salary >= 5000 is: {count}")