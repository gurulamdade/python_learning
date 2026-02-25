employee_ids = (101, 102, 103, 104, 105)
print(employee_ids)
print("First employee ID:", employee_ids[0])
print("Last employee ID:", employee_ids[-1])

# Print middle element
middle_index = len(employee_ids) // 2
print("Middle employee ID:", employee_ids[middle_index])

# Slice last 3 elements
last_three = employee_ids[-3:]
print("Last 3 employee IDs:", last_three)

# Find total number of IDs using len()
print("Total employee IDs:", len(employee_ids))
