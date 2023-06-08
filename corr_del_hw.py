#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных


def changing_csv(file):
    with open(file, encoding='utf-8') as data:
        res = data.readlines()
        string_number = int(input('Введите номер строки для изменения: '))
        last_name_new = input('Введите новую фамилию: ')
        fist_name_new = input('Введите новое имя: ')
        number_new = input('Введите новый номер: ')
        res[string_number] = (f'{last_name_new},{fist_name_new},{number_new}\n')
    with open('phone.csv', 'w', encoding='utf-8') as data:
        data.writelines(res)
    return res


def correction():
    print(changing_csv('phone.csv'))


def delete_line(file):
    with open(file, encoding='utf-8') as data:
        res = data.readlines()
        string_number = int(input('Введите номер строки для удаления: '))
        res[string_number] = ''
    with open('phone.csv', 'w', encoding='utf-8') as data:
        data.writelines(res)
    return res


def removing():
    print(delete_line('phone.csv'))