""" Методы для проверки ответов наших запросов"""
from requests import Response
import json

class Checking():

    """ Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response : Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Успешно Статус код = {str(response.status_code)}')
        else:
            print('Провал')


    """ Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response : Response, expected_value):
        # строчка ниже возвращает все значения словаря
        # token = json.loads(response.text) Есть два создания переменной token слева первый , снизу второй
        # функция лист возвращает все ключи словаря
        token = response.json()
        assert list(token) == expected_value
        print('Все поля присутствует')


    """ Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response : Response,field_name, expected_value):
        check = response.json()
        check_info = check[field_name]
        assert expected_value == check_info
        print(f'{field_name} верен!')





