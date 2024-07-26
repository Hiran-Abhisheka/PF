students = []
for _ in range(5):
    name = input("Enter student name: ")
    students.append(name)

students.sort()

print("First student in alphabetical order:", students[0])
print("Last student in alphabetical order:", students[-1])
