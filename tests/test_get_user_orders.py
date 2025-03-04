import requests

import urls
from data import *

class TestGetUserOrders:
    def test_get_order_user_with_auth(self, response_user_data_token):
        token = {
            'Authorization': response_user_data_token[2]
        }
        requests_create_order = requests.post(f"{urls.MAIN_URL}{urls.Hands.MAKE_ORDER}", headers=token, data=IngredientsData.VALID_HASH)
        response_get_user_orders = requests.get(f"{urls.MAIN_URL}{urls.Hands.GET_ORDERS}", headers=token)
        assert response_get_user_orders.status_code == StatusCodes.CODE_200
        assert response_get_user_orders.json().get('orders')[0].get('number') == requests_create_order.json().get('order').get('number')

    def test_get_order_user_not_auth(self):
        response_get_user_orders = requests.get(f"{urls.MAIN_URL}{urls.Hands.GET_ORDERS}")
        assert response_get_user_orders.status_code == StatusCodes.CODE_401
        assert response_get_user_orders.json().get('message') == Messages.GetUserOrders.NOT_AUTHORIZED