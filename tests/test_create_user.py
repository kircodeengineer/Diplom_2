import pytest
import requests

from data import StatusCodes, Messages
from user_data import User
import urls

class TestCreateUser:

    def test_create_user_success(self, response_user_data_token):
        response = response_user_data_token[0]
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get("success") == True

    def test_create_double_user_error(self, response_user_data_token):
        user_data = response_user_data_token[1]
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
        assert response.status_code == StatusCodes.CODE_403
        assert response.json().get("message") == Messages.CreateUser.USER_EXISTS

    @pytest.mark.parametrize("user_data",
                             [
                                 User.create_user_data_empty_email(),
                                 User.create_user_data_empty_password(),
                                 User.create_user_data_empty_name()
                             ]
                             )
    def test_create_user_empty_data(self, user_data):
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
        assert response.status_code == StatusCodes.CODE_403
        assert response.json().get("message") == Messages.CreateUser.EMPTY_FIELD