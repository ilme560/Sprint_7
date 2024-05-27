import allure
import requests
import random
import string

from data import Urls


class Helpers:

    @allure.step("генерация строки")
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("генерации логина, пароля и имени")
    def generate_data(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)
        return login, password, first_name

    @allure.step('Создаем курьера и получаем логин, пароль и имя')
    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @allure.step('Удаляем курьера')
    def delete_courier(self, login, password):
        response_post = requests.post(Urls.LOGIN_COURIER, data={
            "login": login,
            "password": password,
        })
        courier_id = response_post.json()['id']
        requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')
