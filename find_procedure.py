# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
way_dir = os.path.join(current_dir, migrations)

def read_file(file_name, file_list_new):
    with open(file_name, "r") as file:
        file_read = file.read()
        if find_string in file_read:
            file_list_new.append(file_name)
            print(file_name)
    return file_list_new

def find_procedure(file_list):
    file_list_new = list()
    for file in file_list:
        file_list_new = read_file(file, file_list_new)
    print(len(file_list_new))
    return file_list_new

if __name__ == '__main__':
    file_list = list()
    for root, dirs, files in os.walk(way_dir):
        for filename in files:
            if filename.endswith(".sql"):
                way_file = os.path.join(way_dir, filename)
                file_list.append(way_file)

    while True:
        print(file_list)
        find_string = input("Введите строку поиска")
        file_list = find_procedure(file_list)

    # files = os.listdir(way)                             #способ 2 перебрать файлы
    # mytxt = filter(lambda x: x.endswith('.sql'), files)

