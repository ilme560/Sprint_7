import allure
import requests
from data import Urls, ApiAnswer


class TestLoginCourier:

    @allure.title('Успешная авторизация ')
    @allure.description("Проверка успешной авторизации,статус кода и возврат id ")
    def test_login_courier(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": data[0],
            "password": data[1],
        })
        assert response.status_code == 200
        assert ApiAnswer.LOG_IN_COURIER_SUCCESSFUL in response.text
        helpers.delete_courier(data[0], data[1])

    @allure.title('Авторизация без указания login')
    @allure.description("Проверка ошибки авторизации курьера без указания обязательного поля login")
    def test_login_courier_without_login(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": data[0],
            "password": '',
        })
        assert response.status_code == 400
        assert ApiAnswer.LOG_IN_COURIER_WITHOUT_DATA in response.text

    @allure.title('Авторизация без указания password')
    @allure.description("Проверка ошибки авторизации курьера без указания обязательного поля password")
    def test_login_courier_without_password(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": '',
            "password": data[1],
        })
        assert response.status_code == 400
        assert ApiAnswer.LOG_IN_COURIER_WITHOUT_DATA in response.text

    @allure.title('Авторизация без указания login и password')
    @allure.description("Проверка ошибки авторизации курьера без указания обязательного поля login и password")
    def test_login_courier_without_data(self, helpers):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": '',
            "password": '',
        })
        assert response.status_code == 400
        assert ApiAnswer.LOG_IN_COURIER_WITHOUT_DATA in response.text

    @allure.title('Авторизация авторизоваться под несуществующим пользователем')
    @allure.description("Проверка  ошибки авторизации авторизоваться под несуществующим пользователем")
    def test_login_courier_fake_data(self):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": 'arnold',
            "password": 'stalone',
        })
        assert response.status_code == 404
        assert ApiAnswer.LOG_IN_COURIER_FAKE_DATA in response.text
