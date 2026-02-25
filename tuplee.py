data = (1, 2, 3)
print("Original ID:", id(data))

data = data + (4,)

print("Updated Tuple:", data)
print("New ID:", id(data))

numbers = [10, 20, 30]
print("Original ID:", id(numbers))

numbers.append(40)

print("Updated List:", numbers)
print("ID After Append:", id(numbers))