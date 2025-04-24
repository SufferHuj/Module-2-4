import pytest
import requests

from constants import base_url

class TestBooking:

    def test_create_booking(self, auth_session, booking_data):

        # проверка создания бронирования
        create_bookings = auth_session.post(f"{base_url}/booking", json = booking_data)
        assert create_bookings.status_code == 200, "Ошибка! Неудачное бронирование"

        # проверка наличия id бронирования
        booking_id = create_bookings.json().get("bookingid")
        assert booking_id is not None, "В ответе нет ID бронирования"
        assert create_bookings.json()["booking"]["firstname"] == booking_data["firstname"], "Ошибка! Имя не совпадает"
        assert create_bookings.json()["booking"]["totalprice"] == booking_data["totalprice"], "Ошибка! Сумма не совпадает"

        # проверка получения по id данных о бронирование
        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Ошибка! Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Ошибка! Фамилия не совпадает"

        # проверка удаления бронирования
        delete_booking = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert delete_booking.status_code == 201, "Ошибка! Бронь не удалена"

        # проверка недоступности бронирования после удаления
        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Ошибка! Бронь не удалена"

    def test_update_booking_with_put(self, auth_session, booking_data, update_date):

        # проверка создания бронирования
        create_response = auth_session.post(f"{base_url}/booking", json = booking_data)

        # проверяем наличия id бронирования
        booking_id = create_response.json()["bookingid"]

        # проверка изменения данных бронирования
        put_booking = auth_session.put(f"{base_url}/booking/{booking_id}", json = update_date)
        assert put_booking.status_code == 200, "Ошибка! Неудачное изменение данных бронирования"

        # проверка получения по id данных о бронирование
        get_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_response.status_code == 200, "Ошибка! Бронь не найдена"
        assert get_response.json()["firstname"] == update_date["firstname"], "Ошибка! Имя не обновлено"
        assert get_response.json()["lastname"] == update_date["lastname"], "Ошибка! Фамилия не обновлена"
        assert get_response.json()["totalprice"] == update_date["totalprice"], "Ошибка! Сумма не обновлена"

    def test_update_booking_with_patch(self, auth_session, booking_data, patch_date):

        # проверка создания бронирования
        create_response = auth_session.post(f"{base_url}/booking", json = booking_data)

        # проверяем наличия id бронирования
        booking_id = create_response.json()["bookingid"]

        # проверка частичного изменения данных бронирования
        patch_booking = auth_session.patch(f"{base_url}/booking/{booking_id}", json = patch_date)
        assert patch_booking.status_code == 200, "Ошибка! Неудачное изменение данных бронирования"

        # проверка получения по id данных о бронирование
        get_response = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_response.status_code == 200, "Ошибка! Бронь не найдена"
        assert get_response.json()["firstname"] == patch_date["firstname"], "Ошибка! Имя не обновлено"
        assert get_response.json()["totalprice"] == patch_date["totalprice"], "Ошибка! Сумма не обновлена"

    # НЕГАТИВНЫЕ ПРОВЕРКИ

    # проверка с отправкой невалидных данных
    @pytest.mark.negative
    def test_create_booking_with_invalid_data(self, auth_session, invalid_booking_data):
        response = auth_session.post(f"{base_url}/booking", json = invalid_booking_data)
        assert response.status_code == 500, "Ожидался статус 500 при невалидных данных"

    # проверка обновления несуществующего ресурса
    @pytest.mark.negative
    def test_put_update_nonexistent_booking(self, auth_session, update_date):
        invalid_id = 999000999  # предполагаем, что такого ID нет
        response = auth_session.put(f"{base_url}/booking/{invalid_id}", json=update_date)
        assert response.status_code == 405, "Ожидался 405 для несуществующего ресурса"

    # проверка удаления ресурса без авторизации
    @pytest.mark.negative
    def test_delete_without_auth(self, auth_session, booking_data):
        # создаём бронирование с авторизацией
        create_response = auth_session.post(f"{base_url}/booking", json=booking_data)
        booking_id = create_response.json()["bookingid"]

        # удаляем без авторизации
        response = requests.delete(f"{base_url}/booking/{booking_id}")
        assert response.status_code == 403, "Удаление без токена должно быть запрещено"

    # проверка обновления с пустыми данными в put
    @pytest.mark.negative
    def test_put_with_empty_data(self, auth_session, booking_data):
        create_response = auth_session.post(f"{base_url}/booking", json=booking_data)
        booking_id = create_response.json()["bookingid"]

        response = auth_session.put(f"{base_url}/booking/{booking_id}", json={})
        assert response.status_code in (400, 500), "Ожидался статус ошибки на пустой put"