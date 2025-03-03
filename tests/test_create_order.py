import requests
from data import *
import urls

class TestCreateOrder:
    def test_create_order_with_auth(self, response_user_data_token):
        token = {'Authorization': response_user_data_token[2]}
        r = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", headers=token, data=IngredientsData.VALID_HASH)
        assert r.status_code == StatusCodes.CODE_200
        assert r.json().get('success') is True

    def test_create_order_not_auth(self):
        r = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", data=IngredientsData.VALID_HASH)
        assert r.status_code == StatusCodes.CODE_200
        assert r.json().get('success') is True

    def test_create_order_with_no_ingredient(self):
        r = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}")
        assert r.status_code == StatusCodes.CODE_400
        assert r.json().get('message') == Messages.CreateOrder.NO_INGREDIENTS_PROVIDED

    def test_create_order_invalid_hash_ingredient(self, response_user_data_token):
        token = {'Authorization': response_user_data_token[2]}
        response = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", headers=token, json=IngredientsData.NOT_VALID_HASH)
        assert response.status_code == 500
        assert Messages.INTERNAL_SERVER_ERROR in response.text