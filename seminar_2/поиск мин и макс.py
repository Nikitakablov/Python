# ; Пользователь вводит одно число N – количество
# ; арбузов. Вторая строка содержит N чисел,
# ; записанных на новой строчке каждое. Здесь каждое
# ; число – это масса соответствующего арбуза
# ; Input: 5 -> 5 1 6 5 9
# ; Output: 1 9
n = int(input())
arbuz = int(input('Вес первого арбуза'))
max = arbuz
min = arbuz
for _ in range(n-1):
    arbuz = int(input('Вес арбуза'))
    if arbuz > max:
        max = arbuz
    if arbuz < min:
        min = arbuz
print(f"{max} {min}")