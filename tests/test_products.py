import allure
import requests
from allure_commons.types import Severity
from jsonschema import validate
from schemas.get_brands_list import brands_list
from schemas.get_product_list import product_list
from schemas.post_search_product_without_parameter import search_without_parameter
from utils.attach import add_attach, add_logs


@allure.tag('API')
@allure.feature('Продукты')
class TestProducts:
    @allure.story('Запрос списка всех продуктов')
    @allure.severity(Severity.CRITICAL)
    def test_get_product_list(self, base_url):
        url = base_url + 'api/productsList'
        with allure.step("Отправляем запрос на получение списка всех продуктов"):
            response = requests.get(url)
        with allure.step("Проверка валидности полученной json схемы"):
            validate(response.json(), schema=product_list)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка что полученный список не пустой"):
            assert len(response.json()) > 0
        add_attach(response)
        add_logs(response)

    @allure.story('Запрос списка всех брендов')
    @allure.severity(Severity.NORMAL)
    def test_get_brands_list(self, base_url):
        url = base_url + 'api/brandsList'
        with allure.step("Отправляем запрос на получение списка всех брендов"):
            response = requests.get(url)
        with allure.step("Проверка валидности полученной json схемы"):
            validate(response.json(), schema=brands_list)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка что полученный список не пустой"):
            assert len(response.json()) > 0
        add_attach(response)
        add_logs(response)

    @allure.story('Поиск товаров по категории')
    @allure.severity(Severity.NORMAL)
    def test_search_product_by_category(self, base_url):
        url = base_url + 'api/searchProduct'
        data = {"search_product": "jeans"}
        with allure.step("Отправляем запрос на поиск товаров по категории Jeans"):
            response = requests.post(url, data=data)
        with allure.step("Проверка валидности полученной json схемы"):
            validate(response.json(), schema=product_list)
        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка категорий товаров из полученного списка"):
            for i in response.json()["products"]:
                if i['category']['category'] != "Jeans":
                    print("Категория товара не соответствует искомой")
                    break
        add_attach(response)
        add_logs(response)


    @allure.story('Поиск товаров без указанного параметра категории')
    @allure.severity(Severity.NORMAL)
    def test_search_product_without_category_parameter(self, base_url):
        url = base_url + 'api/searchProduct'
        with allure.step("Отправляем запрос на поиск товаров без указанного параметра категории"):
            response = requests.post(url)
        with allure.step("Проверка валидности полученной json схемы"):
            validate(response.json(), schema=search_without_parameter)
        with allure.step('Проверка статус кода в ответе == 400'):
            assert response.json()["responseCode"] == 400
        add_attach(response)
        add_logs(response)


