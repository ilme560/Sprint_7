import allure
import requests
from data import Urls, ApiAnswer


class TestDeleteCourier:

    @allure.title('Успешное удаление курьера со всеми обязательными полями')
    def test_delete_courier(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response_post = requests.post(Urls.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        id = response_post.json()['id']
        payload = {'id': id}
        response_delete = requests.delete(f'{Urls.DELETE_COURIER}{id}', data=payload)
        assert response_delete.status_code == 200
        assert ApiAnswer.DELETE_COURIER_SUCCESSFUL in response_delete.text

    @allure.title('Удаление курьера без id курьера')
    def test_delete_courier_without_id(self, helpers):
        response_delete = requests.delete(Urls.DELETE_COURIER)
        assert response_delete.status_code == 404
        assert ApiAnswer.DELETE_COURIER_WITHOUT_ID in response_delete.text

    @allure.title('Удаление курьера с несуществующим id курьера')
    def test_delete_courier_fake_id(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response_post = requests.post(Urls.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        id = response_post.json()['id']
        payload = {'id': id}
        response_delete = requests.delete(f'{Urls.DELETE_COURIER}{id}1', data=payload)
        assert response_delete.status_code == 404
        assert ApiAnswer.DELETE_COURIER_FAKE_ID in response_delete.text
