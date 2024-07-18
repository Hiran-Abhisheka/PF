print("Choose an option:")
print("1. Calculate circumference of a circle")
print("2. Calculate area of a circle")
print("3. Calculate volume of a sphere")
print("4. Quit")
  
choice = input("Enter your choice (1/2/3/4): ")
  
if choice == "1":
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * 3.14 * radius
    print("The circumference of the circle is: ", circumference)
elif choice == "2":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print("The area of the circle is: ", area)
elif choice == "3":
    radius = float(input("Enter the radius of the sphere: "))
    sphere = (4/3) * 3.14 * radius ** 3
    print("The volume of the sphere is: ", sphere)
elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")