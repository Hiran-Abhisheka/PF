x=int(input("Parameter 1: "))
y=int(input("Parameter 2: "))
z=int(input("Parameter 3: "))

if z!=0:
    out=pow(x,y)%z
    print("----------------------------------------------------------------\n"
    f"Parameter 1: {x}, Parameter 2: {y}, Parameter 3: {z}, Output: {out}\n"
    "------------------------------------------------------------------")
else:
    print("----------------------\n"
    "    ERROR\n"
    "-------------------------")

