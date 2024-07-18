marks = []
for i in range(1, 11):
    mark = float(input(f"Enter marks of student {i}: "))
    marks.append(mark)
max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / len(marks)
print(f"Maximum Mark: {max_mark}")
print(f"Minimum Mark: {min_mark}")
print(f"Average Mark: {avg_mark}")
