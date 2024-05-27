class Urls:
    URL = 'http://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{URL}/api/v1/courier'
    LOGIN_COURIER = f'{URL}/api/v1/courier/login'
    CREATE_ORDER = f'{URL}/api/v1/orders'
    ORDER_LIST = f'{URL}/api/v1/orders'
    DELETE_COURIER = f'{URL}/api/v1/courier/'
    GET_ORDER_TRACK = f'{URL}/api/v1/orders/track'
    TAKE_ORDER = f'{URL}/api/v1/orders/accept/'


class ApiAnswer:
    CREATE_COURIER_SUCCESSFUL = '{"ok":true}'
    CREATE_COURIER_AGAIN = 'Этот логин уже используется'
    CREATE_COURIER_WITHOUT_LOGIN = 'Недостаточно данных для создания учетной записи'
    LOG_IN_COURIER_SUCCESSFUL = 'id'
    LOG_IN_COURIER_WITHOUT_DATA = 'Недостаточно данных для входа'
    LOG_IN_COURIER_FAKE_DATA = 'Учетная запись не найдена'
    CREATE_ORDER_SUCCESSFUL = 'track'
    LIST_ORDERS_SUCCESSFUL = 'orders'
    DELETE_COURIER_SUCCESSFUL = '{"ok":true}'
    DELETE_COURIER_WITHOUT_ID = 'Not Found.'
    DELETE_COURIER_FAKE_ID = 'Курьера с таким id нет'


class UserDataForTest:

    user_data = [
        ['Arnold', 'Schwarzenegger', 'Sverdlova, 16', '5', '+7 912 680 50 51', '3', '2024-06-06', 'I ll be back', "BLACK"],
        ['Sylvester', 'Stallone', 'Sverdlova, 17', '4', '+7 912 680 50 55', '2', '2024-06-06', 'I ll be back', "GREY"],
        ['Chuck', 'Norris', 'Sverdlova, 18', '3', '+7 912 680 50 53', '1', '2024-06-06', 'I ll be back', "BLACK, GREY"],
        ['Jean Claude', 'van Dam', 'Sverdlova, 19', '5', '+7 912 680 50 54', '4', '2024-06-06', 'I ll be back', ""]
    ]
