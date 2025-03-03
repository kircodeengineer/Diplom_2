import requests
import pytest
import urls

from data import StatusCodes, Messages

class TestChangUserData:
    @pytest.mark.parametrize('change_field', ['email', 'name'])
    def test_changing_user_data_with_auth(self, response_user_data_token, change_field):
        payload = {
            change_field : response_user_data_token[1][change_field] + '1'
        }
        token = {
            'Authorization': response_user_data_token[2]
        }
        response = requests.patch(f"{urls.MAIN_URL}{urls.Hands.CHANGE_USER_DATA}", headers=token, data=payload)
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('user').get(change_field) == payload[change_field]


    def test_changing_user_data_password_with_auth(self, response_user_data_token):
        payload = {
            'password' : response_user_data_token[1]['password'] + '1'
        }
        token = {
            'Authorization': response_user_data_token[2]
        }
        response = requests.patch(f"{urls.MAIN_URL}{urls.Hands.CHANGE_USER_DATA}", headers=token, data=payload)
        assert response.status_code == StatusCodes.CODE_200
        assert response.json().get('success') == True

    @pytest.mark.parametrize('change_field', ['email', 'name', 'password'])
    def test_changing_user_data_no_auth(self, response_user_data_token, change_field):
        payload = {
            change_field: response_user_data_token[1][change_field]
        }
        response = requests.patch(f"{urls.MAIN_URL}{urls.Hands.CHANGE_USER_DATA}", data=payload)
        assert response.status_code == StatusCodes.CODE_401
        assert response.json().get('message') == Messages.ChangeUserData.NOT_AUTHORIZED
