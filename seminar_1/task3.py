year = int(input("Введите год: "))
if ((year%4 == 0) and (year != year%100)) or (year%400 == 0):
    print('Yes')
else:
    print('No')

# тернарный оператор 
# print ("yes" if ((a%4 == 0) and (a%100 != 0)) or (a%400 == 0) else "nooooooo")
