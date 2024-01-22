import json
from datetime import datetime

def open_file(json_file):
    '''
    Открывает и возвращает файл JSON
    '''
    with open(json_file) as file:
        operation = json.load(file)
    return operation

def completed_operation(operation):
    '''Выдает список выполненных операций'''
    new_operation = []
    for i in operation:
        if i.get('state') == 'EXECUTED':
            new_operation.append(i)
        else:
            continue
    return new_operation


def sort_data(operation):
    """ сортировка файла по дате """
    sort_data = sorted(operation, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    last_operation = sort_data[:5]
    return last_operation

def hide_cart_number(cart_number):
    '''

    :param cart_number: Maestro 9171987821259925
    :return: 9171 98** **** 9925
    '''
    a = cart_number.split()
    index = len(str(a[-1])) // 4
    index2 = index * 2
    index3 = index * 3
    first_part = str(a[-1])[:index]
    second_part = str(a[-1])[index:index2]
    second_part_hide = second_part[0:2] + '**'
    third_part = '****'
    fourth_part = str(a[-1])[index3:]
    fin_number = first_part + " " + second_part_hide + " " + third_part + " " + fourth_part
    return fin_number


def hide_account_number(account_number):
    '''

    :param account_number: Счет 97848259954268659635
    :return: **9635
    '''
    a = account_number.split()
    fin_number = "**" + str(a[1])[-4:]
    return fin_number


def date_format(date):
    in_data = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    format_date = f"{in_data:%d.%m.%Y}"
    return format_date


