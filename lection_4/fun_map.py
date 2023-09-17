# Функция map
# 💡 Функция map() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с новыми объектами.

# Есть набор данных. Функция map позволяет увеличить каждый объект на 10.
# list_1 = [x for x in range (1,20)]
# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел? 
# Решение:
# data = '1 2 3 5 8 15 23 38'
# # data = list(map(int,data.split()))
# # print(data)

# 1.отступление, функция строка.split() - убирает все пробелы и создаем
# список из значений строки, пример:
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int,data.split()))
# print(data)

# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

#  Теперь вернемся к задаче. С помощью функции map():
# data = list(map(int,input().split()))
# Результат работы map() — это итератор. По итератору можно пробежаться только
# один раз. Чтобы работать несколько раз с одними данными, нужно сохранить
# данные (например, в виде списка).

