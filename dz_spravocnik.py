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

"""Вывод на экран справочника"""
def print_sprav(sprav):
    for item in sprav:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))
   
def main (sprav):
    while True:
        print(f"""\nЧто хотите сделать?
        1: Вывести данные
        2: Записать новый контакт
        3: Найти контакт по полю 'фамилия'
        4: Скопировать строку по 'id' в новый файл
        0: Сохранить и выйти""")
        
        x = input()
        if x == '1':
            print_sprav(sprav)
        elif x == '0':
            break
        else:
            print('Неверная команда!')
            
if __name__ == "__main__":
    main(open_sprav())