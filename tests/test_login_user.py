import pytest
import requests

from data import *
import urls


class TestLogin:
    def test_login_user(self, response_user_data_token):
        email_pass = response_user_data_token[1]
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.LOGIN}', data=email_pass)
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('success') == True

    @pytest.mark.parametrize("wrong_field", ["email", "password"])
    def test_login_user_error(self, response_user_data_token, wrong_field):
        email_pass = response_user_data_token[1]
        email_pass[wrong_field] += "1"
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.LOGIN}', data=email_pass)
        assert response.status_code == StatusCodes.CODE_401
        assert response.json().get('message') == Messages.Login.INCORRECT_USER_DATA