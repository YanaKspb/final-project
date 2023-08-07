import requests
import configuration
import data


# Функция для создания заказа

def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body,
                         headers=data.headers)


# Функция для получения номера трека заказа

def get_track_number():
    result = post_create_order(data.order).json()
    track_number = dict(result)
    track_numbers = track_number["track"]
    return track_numbers


# Вставляем трек заказа в запрос
track = str(get_track_number())
ORDER_BY_CURRENT_TRACK = "/api/v1/orders/track?t=" + track


# Функция для получения информации о заказе по треку

def get_created_order():
    return requests.get(configuration.URL_SERVICE + ORDER_BY_CURRENT_TRACK)

