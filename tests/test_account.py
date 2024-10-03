import os
import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate
from utils.attach import add_attach, add_logs
from utils.generate_email import email_generate
from schemas.post_create_user import create_user
from schemas.post_login_user import login_user


@allure.tag('API')
@allure.feature('Аккаунт')
class TestUserAccount:
    @allure.story('Регистрация нового пользователя')
    @allure.severity(Severity.CRITICAL)
    def test_register_user(self, base_url):
        url = base_url + 'api/createAccount'
        data = {
            "name": "Justin Bieber",
            "email": email_generate(),
            "password": "qwerty123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "03",
            "birth_year": "1990",
            "firstname": "Justin",
            "lastname": "Bieber",
            "company": "Warner Brosers",
            "address1": "Los Angeles",
            "address2": "New York",
            "country": "USA",
            "zipcode": "123",
            "state": "California",
            "city": "Brooklin",
            "mobile_number": "85729874134"
        }
        with allure.step('Отправлем запрос на регистрацию'):
            response = requests.post(url, data=data)
        with allure.step('Проверка валидности полученной json схемы'):
            validate(response.json(), schema=create_user)
        with allure.step('Проверка статус кода в ответе == 201'):
            assert response.json()["responseCode"] == 201
        with allure.step('Проверка сообщения об успешной регистрации'):
            assert response.json()['message'] == 'User created!'
        add_attach(response)
        add_logs(response)

    @allure.story('Авторизация пользователя с валидными данными')
    @allure.severity(Severity.CRITICAL)
    def test_login_with_valid_data(self, base_url):
        url = base_url + 'api/verifyLogin'
        data = {"email": os.getenv('EMAIL'), "password": os.getenv('PASSWORD')}
        with allure.step('Отправляем запрос на авторизацию с валидными данными'):
            response = requests.post(url, data=data)
        with allure.step('Проверка валидности полученной json схемы'):
            validate(response.json(), schema=login_user)
        with allure.step('Проверка статус кода в ответе == 200'):
            assert response.status_code == 200
        with allure.step('Проверка сообщения об успешной авторизации'):
            assert response.json()["message"] == "User exists!"
        add_attach(response)
        add_logs(response)

    @allure.story('Авторизация пользователя с невалидными данными')
    @allure.severity(Severity.CRITICAL)
    def test_login_with_invalid_data(self, base_url):
        url = base_url + 'api/verifyLogin'
        data = {"email": "justin1@gmail.com", "password": "qwerty123fsdfsdf"}
        with allure.step('Отправляем запрос на авторизацию с валидными данными'):
            response = requests.post(url, data=data)
        with allure.step('Проверка валидности полученной json схемы'):
            validate(response.json(), schema=create_user)
        with allure.step('Проверка статус кода в ответе == 404'):
            assert response.json()["responseCode"] == 404
        with allure.step('Проверка сообщения об ошибке авторизации'):
            assert response.json()["message"] == "User not found!"
        add_attach(response)
        add_logs(response)