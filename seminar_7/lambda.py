values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# transormed_values = values[:]
print(values)
# print(transormed_values)

# transformation = lambda item: item
transformation_values = list(map(lambda item: item, values))

print(transformation_values)

# Все четные умножить на 3, все нечетные разделить на 5

print(list(map(lambda x: x / 5 if (x % 2) else x * 3, [1, 5, 8, 3, 6, 10])))