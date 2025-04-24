import copy
import pytest
import requests
from datetime import timedelta
from faker import Faker
from constants import base_url, headers, auth_data

faker = Faker()

@pytest.fixture
def date_range():
    checkin = faker.date_between(start_date="today", end_date="+30d")
    checkout = checkin + timedelta(days=faker.random_int(min=1, max=14))
    return checkin.isoformat(), checkout.isoformat()

@pytest.fixture(scope="session")
def auth_session():

    session_x = requests.Session()
    session_x.headers.update(headers)

    response = requests.post(f"{base_url}/auth", headers= headers, json= auth_data)
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не указан токен"

    session_x.headers.update({"Cookie": f"token={token}"})
    return session_x

@pytest.fixture
def booking_data(date_range):
    checkin, checkout = date_range
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min = 100, max = 100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": "Piano"
        }

@pytest.fixture
def update_date(booking_data):
    updated_data = copy.deepcopy(booking_data)
    updated_data["firstname"] = faker.first_name()
    updated_data["lastname"] = faker.last_name()
    updated_data["totalprice"] = faker.random_int(min = 100, max = 100000)
    return updated_data

@pytest.fixture
def patch_date(booking_data):
    patched_date = copy.deepcopy(booking_data)
    patched_date["firstname"] = faker.first_name()
    patched_date["totalprice"] = faker.random_int(min=100, max=100000)
    return patched_date

@pytest.fixture
def invalid_booking_data(booking_data):
    return {
        # пропущен lastname, и totalprice — строка
        "firstname": "",
        "totalprice": "много",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "not-a-date",
            "checkout": "also-wrong"
        },
        "additionalneeds": " "
    }