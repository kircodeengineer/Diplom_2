import requests
import pytest
from user_data import User
import urls

@pytest.fixture()
def response_user_data_token():
    user_data = User.create_user_data()
    response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
    token = response.json().get("accessToken")
    yield response, user_data, token
    requests.delete(f'{urls.MAIN_URL}{urls.Hands.DELETE_USER}', headers={'Authorization': f'{token}'})