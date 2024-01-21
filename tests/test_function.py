
from src.function import *

def test_completed_operation():
    operaion = [{"id": 121646999, "state": "CANCELED", "date": "2018-06-08T16:14:59.936274"},
                {"id": 736942989, "state": "EXECUTED", "date": "2019-09-06T00:48:01.081967"},
                {"id": 27192367, "state": "CANCELED", "date": "2018-12-24T20:16:18.819037"}]
    assert completed_operation(operaion) == [{"id": 736942989, "state": "EXECUTED", "date": "2019-09-06T00:48:01.081967"}]

def test_sort_data():
    operaion = [{"id": 121646999, "state": "CANCELED", "date": "2018-06-08T16:14:59.936274"},
                {"id": 736942989, "state": "EXECUTED", "date": "2019-09-06T00:48:01.081967"},
                {"id": 27192367, "state": "CANCELED", "date": "2018-12-24T20:16:18.819037"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]
    assert sort_data(operaion) == [{"id": 736942989, "state": "EXECUTED", "date": "2019-09-06T00:48:01.081967"},
                                   {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
                                   {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                   {"id": 27192367, "state": "CANCELED", "date": "2018-12-24T20:16:18.819037"},
                                   {"id": 121646999, "state": "CANCELED", "date": "2018-06-08T16:14:59.936274"}]


def test_hide_cart_number():
    assert hide_cart_number("Visa Platinum 1813166339376336") == '1813 16** **** 6336'
    assert hide_cart_number("Maestro 9171987821259925") == '9171 98** **** 9925'
    assert hide_cart_number("Maestro 1913883747791351") == '1913 88** **** 1351'


def test_hide_account_number():
    assert hide_account_number("Счет 72645194281643232984") == '**2984'
    assert hide_account_number("Счет 95782287258966264115") == '**4115'
    assert hide_account_number("Счет 46878338893256147528") == '**7528'

def test_date_format():
    assert date_format('2018-06-08T16:14:59.936274') == '08.06.2018'
    assert date_format('2019-09-06T00:48:01.081967') == '06.09.2019'
    assert date_format('2019-07-03T18:35:29.512364') == '03.07.2019'