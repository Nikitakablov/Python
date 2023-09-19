# Создать телефонный справочник с возможностью импорта и экспорта 
# данных в формате .txt. Фамилия, имя, отчество, номер 
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные втекстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Функция для добавления новой записи в справочник
# phonebook = []

# def add_contact_and_export(last_name, first_name, middle_name, phone_number):
#     with open('directory.txt', 'w') as f:
#         f.write(f'\n{last_name}, {first_name},{middle_name}, {phone_number}')

# print(add_contact_and_export())
def write_person(second_name, first_name, phone):
    with open('directory.txt', 'a') as f:
        f.write(f'{second_name}, {first_name}, {phone}\n')

def write_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    write_person(second_name, first_name, phone)

def display_directory():
    with open('directory.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_person():
    search_term = input('Введите характеристику для поиска (фамилия, имя или номер телефона): ')
    with open('directory.txt', 'r') as f:
        found = False
        for line in f:
            second_name, first_name, phone = line.strip().split(', ')
            if search_term in [second_name, first_name, phone]:
                print(line.strip())
                found = True
        if not found:
            print('Запись не найдена.')

def export_data():
    with open('directory.txt', 'r') as source, open('exported_directory.txt', 'w') as dest:
        for line in source:
            dest.write(line)

def update_person():
    search_term = input('Введите характеристику для поиска (фамилия, имя или номер телефона) записи, которую вы хотите изменить: ')
    updated_data = input('Введите новые данные в формате "Фамилия, Имя, Номер телефона": ')
    
    with open('directory.txt', 'r') as source, open('temp.txt', 'w') as dest:
        updated = False
        for line in source:
            second_name, first_name, phone = line.strip().split(', ')
            if search_term in [second_name, first_name, phone]:
                dest.write(updated_data + '\n')
                updated = True
            else:
                dest.write(line)
        
    if updated:
        os.remove('directory.txt')
        os.rename('temp.txt', 'directory.txt')
        print('Запись обновлена.')
    else:
        print('Запись не найдена.')

while True:
    print("\nМеню:")
    print("1. Добавить новую запись")
    print("2. Вывести все записи")
    print("3. Найти запись")
    print("4. Экспортировать данные")
    print("5. Изменить запись")
    print("6. Удалить запись")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        write_data()
    elif choice == '2':
        display_directory()
    elif choice == '3':
        search_person()
    elif choice == '4':
        export_data()
    elif choice == '5':
        update_person()
    elif choice == '6':
        delete_person()
    elif choice == '7':
        break
    else:
        print('Неверный выбор. Попробуйте снова.')

