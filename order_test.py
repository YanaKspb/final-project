import create_order


# Функция для проверки кода ответа по запросу  на получения заказа по треку заказа

def test_check_order_by_track():
    response = create_order.get_created_order()

    assert response.status_code == 200


# Яна Городянская, 7-я когорта — Финальный проект. Инженер по тестированию плюс
