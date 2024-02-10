"""
Задача №49. 
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
"""

FILE_NAME = 'tel_sprav.txt'
HEADERS = ['id', 'фамилия', 'имя', 'отчество', 'телефон']

"""Открываем справочник"""
def open_sprav(file_name=FILE_NAME):
    sprav = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            row = [i] + line.strip().split()
            sprav.append(dict(zip(HEADERS, row)))
    return sprav

"""1. Вывод на экран справочника"""
def print_sprav(sprav):
    for item in sprav:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))
        
"""2. Добавляем новый кантакт""" 
def add_contact(sprav):
    row = input ('Введите Ф.И.О. и телефон, резделенные пробелами: ').split()
    line = [len (sprav) + 1] + [item.strip().capitalize() for item in row]
    sprav.append(dict(zip(HEADERS, line)))

"""0. Сохраняем контакт перед выходом"""
def save_contact(directory: list[dict[str, str]], file_name=FILE_NAME):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in directory:
            file.write(' '.join(f'{value}' for key, value in item.items() if key != 'id') + '\n')

"""3. Поиск контакта по ключу"""
def find_contact(key: str, value: str, directory: list[dict[str, str]]):
    for item in directory:
        if item[key] == value:
            print(item)
            
"""4. Копирем данные в файл new_sprav.txt."""
def copy_contact(number, directory):
    if number.isdigit() and (id_ := int (number)) <= len (directory):
        print(*(f" {k}: {v:<16}" for k, v in directory[id_ - 1].items()))
        save_contact([directory[id_ - 1]], file_name= 'new_sprav.txt')
    else:
        print('Нет такого id')
 
def main (sprav):
    while True:
        print(f"""\nЧто хотите сделать?
        1: Вывести данные
        2: Записать новый контакт
        3: Найти контакт по полю 'фамилия'
        4: Скопировать данные по 'id' в новый файл
        0: Сохранить и выйти""")
        
        x = input()
        if x == '1':
            print_sprav(sprav)
        elif x == '2':
            add_contact(sprav)
        elif x == '3':
            last_name = 'фамилия'
            find_contact(key=last_name, value=input(f'{last_name.title()}: ').strip().capitalize(), directory=sprav)
        elif x == '4':
            copy_contact(number=input('Введите id, который хотите скопировать в отедльный файл: '), directory=sprav)
        elif x == '0':
            save_contact(sprav)
            break
        else:
            print('Неверная команда!')
            
if __name__ == "__main__":
    main(open_sprav())