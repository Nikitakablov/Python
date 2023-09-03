# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
already_seen = [] #Здесь создается пустой список already_seen, который будет использоваться для хранения уникальных элементов из my_list.
for item in my_list: #Этот цикл выполняет итерацию по каждому элементу item в списке my_list.
    if item not in already_seen: # В этой строке кода проверяется, содержится ли item в списке already_seen. Если item еще не был добавлен, то код продолжает выполнение.
        already_seen.append(item) # Здесь уникальный элемент item добавляется в список already_seen, чтобы он больше не рассматривался как дубликат.
print(len(already_seen))

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# already_seen = []

# for i in range(len(my_list)):
#     for j in range(len(already_seen)):
#         if my_list[i] == already_seen[j]:
#             break
#     else:
#         already_seen.append(my_list[i])

# print(len(already_seen))

# решение через срез
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0 # Переменная count будет использоваться для подсчета уникальных элементов.
# for i in range (len(list_1)): #Этот цикл выполняет итерацию по индексам элементов в списке list_1.
#     if (list_1[i]) not in list_1[:i]: # В этой строке проверяется, есть ли текущий элемент list_1[i] в срезе списка list_1 до индекса i. Если элемент не находится в этом срезе, это означает, что он уникален, и код увеличивает значение переменной count на 1.
#         count += 1
# print (count)

# решение с помощю множества
# list_1 = set(list_1)
# print (len(list_1))
