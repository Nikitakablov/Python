# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
a = int(input())
i = 2
fib_1 = 0
fib_2 = 1
while fib_2 < a:
    fib_1, fib_2 = fib_2, fib_1 + fib_2
# buff = fib_2
# fib_2 = fib_1 + fib_2
# fib_1 = buff
    i += 1
print(i) if fib_2 == a else print(-1)
# if fib_2 == a:
#     print(i)
# else:
#     print(-1)