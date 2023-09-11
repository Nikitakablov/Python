# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
    #     0   1  2  3   4   5  6  7   8  9  10 11  12 13  14  15 16  17  18  19
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = int(input("Задайте минимальный элемент диапазона: "))
max_value = int(input("Задайте максимальный элемент диапазона: "))
my_list = []
for i in range(len(list_1)):
    if min_value <= list_1[i] <= max_value:
        my_list.append(i)

print(f"Индексы элементов в диапазоне от {min_value} до {max_value}: {my_list}")