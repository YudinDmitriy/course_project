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
    sort_data = sorted(operation, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    last_operation = sort_data[:5]
    return last_operation

def hide_cart_number(cart_number):
    '''

    :param cart_number: 9171987821259925
    :return: 9171 98** **** 9925
    '''
    index = len(str(cart_number)) // 4
    index2 = index * 2
    index3 = index * 3
    first_part = str(cart_number)[:index]
    second_part = str(cart_number)[index:index2]
    second_part_hide = second_part[0:2] + '**'
    third_part = '****'
    fourth_part = str(cart_number)[index3:]
    fin_number = str(first_part) + " " + str(second_part_hide) + " " + third_part + " " + fourth_part
    return fin_number


def hide_account_number(account_number):
    '''

    :param account_number: 97848259954268659635
    :return: **9635
    '''
    fin_number = "**" + str(account_number)[-4:]
    return fin_number


