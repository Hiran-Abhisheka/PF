empno=0
morethan_4000=0
lessthan_4000=0

while True:
    empno=int(input("Enter employee number(-999 to exit): "))
    if empno==-999:
        break
    else:
        hours_worked=float(input("Worked time: "))
        if hours_worked<=40:
            pay=hours_worked*150
        else:
            pay=40*150+(hours_worked-40)*200
    if pay > 4000:
        morethan_4000 += 1
    else:
        lessthan_4000 += 1
    print(f"Employee Number: {empno}, Overtime Payment: Rs. {pay}")
total=morethan_4000+lessthan_4000
percentage=(morethan_4000/total)*100
print(f"Percentage: {percentage}%")