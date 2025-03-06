import allure
import pytest
import requests

from data import *
from user_data import User
import urls


class TestCreateUser:
    @allure.title('Создать уникального пользователя')
    def test_create_user_success(self, response_user_data_token):
        response = response_user_data_token[0]
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('success')

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_create_double_user_error(self, response_user_data_token):
        user_data = response_user_data_token[1]
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
        assert response.status_code == StatusCodes.CODE_403
        assert response.json().get('message') == Messages.CreateUser.USER_EXISTS

    @allure.title('создать пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize("user_data",
                             [
                                 User.create_user_data_no_email(),
                                 User.create_user_data_no_password(),
                                 User.create_user_data_no_name()
                             ]
                             )
    def test_create_user_empty_data(self, user_data):
        response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
        assert response.status_code == StatusCodes.CODE_403
        assert response.json().get('message') == Messages.CreateUser.EMPTY_FIELD