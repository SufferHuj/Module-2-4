import requests

def test_google():
    url = 'https://restful-booker.herokuapp.com/booking'

    payload = {
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

    response = requests.post(url, json=payload)
    assert response.status_code == 200

    print(response.text)
