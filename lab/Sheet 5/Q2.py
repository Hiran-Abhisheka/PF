total=0
for i in range(1,10):
    mark=int(input(f"{i} Enter marks: "))
    
    total+=mark
print(" Total marks: ", total)
avg=total/10
if avg>50:
    print("Pass\n", avg, "%")
else:
    print("Fail\n", avg, "%")