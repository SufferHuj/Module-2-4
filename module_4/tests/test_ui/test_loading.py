import requests

# def test_booking_id():
#     booking_id = 1
#     response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
#
#     data = response.json()
#
#     # Тело ответа в словаре
#     print(f"Тело ответа: {data}")
#     print(response.status_code)
#
#     assert 'firstname' in data

def test_post_request():

    url = "https://restful-booker.herokuapp.com/booking"

    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-04",
            "checkout": "2025-01-15"
        },
        "additionalneeds": "Breakfast"
    }

    # отправляем наш запрос
    response = requests.post(url, json=data)
    assert response.status_code == 200
    print(response.json())

    booking_id = response.json()["bookingid"]

    get_response = requests.get(f"{url}/{booking_id}")
    assert get_response.status_code == 200

    result = get_response.json()
    assert result["firstname"] == data["firstname"]
    print(get_response.request.headers)





