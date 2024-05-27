import allure
import requests
from data import ApiAnswer, Urls


class TestCreateCourier:

    @allure.title('Успешное создание курьера с заполнением всех обязательных полей')
    @allure.description("Создание курьера, проверка кода и текста ответа")
    def test_create_courier(self, helpers):
        login, password, first_name = helpers.generate_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            }
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201
        assert ApiAnswer.CREATE_COURIER_SUCCESSFUL in response.text
        helpers.delete_courier(login, password)

    @allure.title("Невозможно создать двух одинаковых курьеров")
    @allure.description("Проверка статус кода и текста ошибки при создании курьеров с одинаковыми логинами и паролями")
    def test_create_courier_twice(self, helpers):
        data = helpers.register_new_courier_and_return_login_password()
        response = requests.post(Urls.CREATE_COURIER, data={
            "login": data[0],
            "password": data[1],
            "firstName": data[2]
        })
        assert response.status_code == 409
        assert ApiAnswer.CREATE_COURIER_AGAIN in response.text

    @allure.title("Попытка создать курьера без указания login")
    @allure.description(
        "Проверка статус кода и текста ошибки  при попытки создания курьера без обязательного поля login")
    def test_create_courier_without_login(self, helpers):
        login, password, first_name = helpers.generate_data()
        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert ApiAnswer.CREATE_COURIER_WITHOUT_LOGIN in response.text

    @allure.title("Попытка создать курьера без указания password")
    @allure.description(
        "Проверка статус кода и текста ошибки  при попытки создания курьера без обязательного поля password")
    def test_create_courier_without_password(self, helpers):
        login, password, first_name = helpers.generate_data()
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert ApiAnswer.CREATE_COURIER_WITHOUT_LOGIN in response.text

    @allure.title("Попытка создать курьера без указания firstName")
    @allure.description(
        "Проверка статус кода и текста ошибки  при попытки создания курьера без обязательного поля firstName")
    def test_create_courier_without_first_name(self, helpers):
        login, password, first_name = helpers.generate_data()
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        assert response.status_code == 201
        assert ApiAnswer.CREATE_COURIER_SUCCESSFUL in response.text
        helpers.delete_courier(login, password)
