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
