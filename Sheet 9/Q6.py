# Lists of marks
group1_marks = [85, 92, 78, 88, 95]
group2_marks = [90, 83, 87, 79, 91]

# a. Combining lists using extend() method
combined_marks_extend = group1_marks.copy()
combined_marks_extend.extend(group2_marks)
print("Combined marks using extend():", combined_marks_extend)

# b. Combining lists using list operators
combined_marks_operator = group1_marks + group2_marks
print("Combined marks using list operators:", combined_marks_operator)

# II. Sorting the combined marks and printing the highest mark
sorted_combined_marks = sorted(combined_marks_operator)
highest_mark = sorted_combined_marks[-1]
print("Sorted combined marks:", sorted_combined_marks)
print("Highest mark obtained by any student:", highest_mark)
