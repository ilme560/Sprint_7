import allure
import pytest
import requests
from data import Urls, ApiAnswer, UserDataForTest


class TestCreateOrder:

    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color", UserDataForTest.user_data)
    @allure.title('Создание заказа ')
    @allure.description("Проверка успешного создания заказа,статус кода и тело ответа содержит track ")
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                     comment, color):
        data = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        response = requests.post(Urls.CREATE_ORDER, json=data)
        assert response.status_code == 201
        assert ApiAnswer.CREATE_ORDER_SUCCESSFUL in response.text
