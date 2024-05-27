import pytest
import requests

from data import Urls
from data import UserDataForTest
from helpers import Helpers


@pytest.fixture(scope='function')
def helpers():
    return Helpers()


@pytest.fixture(scope='function')
def create_order():
    response_create_order = requests.post(Urls.CREATE_ORDER, json=UserDataForTest.user_data)
    track = response_create_order.json()['track']
    return track


@pytest.fixture(scope='function')
def take_id_order(create_order):
    track = create_order
    response_get_id_order = requests.get(f'{Urls.GET_ORDER_TRACK}?t={track}')
    id_order = response_get_id_order.json()['order']['id']
    return id_order


@pytest.fixture(scope='function')
def create_courier(helpers):
    data = helpers.register_new_courier_and_return_login_password()
    response_post = requests.post(Urls.LOGIN_COURIER, data={
        "login": data[0],
        "password": data[1],
    })
    courier_id = response_post.json()['id']
    yield courier_id
    requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')
