import requests
import pytest
from user_data import User
import urls

@pytest.fixture()
def response_email_pass():
    user_data = User.create_user_data()
    response = requests.post(f'{urls.MAIN_URL}{urls.Hands.CREATE_USER}', data=user_data)
    email_pass = {
        'email': user_data['email'],
        'password': user_data['password']
    }
    yield response, email_pass
    token = response.json().get("accessToken")
    requests.delete(f'{urls.MAIN_URL}{urls.Hands.DELETE_USER}', headers={'Authorization': f'{token}'})