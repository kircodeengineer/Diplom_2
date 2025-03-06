import allure
import requests

from data import *
import urls

class TestCreateOrder:
    @allure.title('Создание заказа c авторизацией и верным хешем ингредиентов')
    def test_create_order_with_auth(self, response_user_data_token):
        token = {'Authorization': response_user_data_token[2]}
        response = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", headers=token, data=IngredientsData.VALID_HASH)
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('success')

    @allure.title('Создание заказа без авторизации и верным хешем ингредиентов')
    def test_create_order_not_auth(self):
        response = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", data=IngredientsData.VALID_HASH)
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('success')

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_with_no_ingredient(self):
        response = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}")
        assert response.status_code == StatusCodes.CODE_400
        assert response.json().get('message') == Messages.CreateOrder.NO_INGREDIENTS_PROVIDED

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_not_valid_hash_ingredient(self, response_user_data_token):
        token = {
            'Authorization': response_user_data_token[2]
        }
        response = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", headers=token, json=IngredientsData.NOT_VALID_HASH)
        assert response.status_code == 500
        assert Messages.INTERNAL_SERVER_ERROR in response.text