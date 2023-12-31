# my_str = "Hellow world"
# print (my_str.split())
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
start_str = 'a a a b c a a d c d d'.split()
print(start_str)

char_dict = {} #: Создается пустой словарь char_dict, который будет использоваться для отслеживания, сколько раз каждое слово уже встречалось.
result_str = '' # Создается пустая строка result_str, в которой мы будем формировать результат.

for char in start_str: # Запускается цикл for, который будет перебирать каждое слово (или символ) в списке start_str.
    if char not in char_dict: # Это условное выражение проверяет, есть ли текущее слово char в словаре char_dict. Если слово ещё не встречалось (его нет в словаре), выполняется следующее
        char_dict[char] = 1 #  Добавляется запись в словарь char_dict, где ключом является текущее слово char, а значением устанавливается 1, что означает, что слово встретилось впервые.
        result_str += f'{char} '
    else:
        result_str += f'{char}_{char_dict[char]} '
        char_dict[char] += 1
print(result_str)