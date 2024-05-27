import allure
import requests
from data import Urls, ApiAnswer


class TestGetOrderList:

    @allure.title('Получение списка  заказов ')
    @allure.description("Проверка получения списка заказов, статус кода и в тексте ответа есть orders ")
    def test_get_order_list(self):
        response = requests.get(Urls.ORDER_LIST)
        assert response.status_code == 200
        assert ApiAnswer.LIST_ORDERS_SUCCESSFUL in response.text
