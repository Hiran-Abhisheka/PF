# Creating the initial list
initial_list = [1, 2, 3]

# I. Using loops (nested loops)
repeated_list_loops = []
for _ in range(3):
    for item in initial_list:
        repeated_list_loops.append(item)
print("Output using loops:", repeated_list_loops)

# II. Using + operator
repeated_list_plus = initial_list + initial_list + initial_list
print("Output using + operator:", repeated_list_plus)

# III. Using * operator
repeated_list_multiply = initial_list * 3
print("Output using * operator:", repeated_list_multiply)
