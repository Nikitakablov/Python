# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# k = 2
# -5 -4 -3 -2 -1
# 0 1 2 3 4
my_list = [1, 2, 3, 4, 5]
# 3, 4, 5, 1, 2
# 4, 5, 1, 2, 3

k = int(input('-> '))
k %= len(my_list) # Эта строка выполняет операцию остатка от деления k на длину списка my_list. Это нужно, чтобы убедиться, что k находится в допустимом диапазоне и избежать лишних сдвигов, если k больше длины списка.
print(my_list[-k:] + my_list[:-k])
#Предположим, что у вас есть список my_list равный [1, 2, 3, 4, 5], 
# и k равно 2 (целочисленный ввод от пользователя).
# my_list[-k:] - это срез последних k элементов из списка.
#  При k = 2 это будут последние два элемента списка [4, 5].
# my_list[:-k] - это срез элементов списка от начала (индекс 0) 
# до k с конца. При k = 2 это будут все элементы, кроме последних двух элементов, 
# то есть [1, 2, 3].