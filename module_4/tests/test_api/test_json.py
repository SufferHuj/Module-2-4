import requests

def test_urls_response():
    urls = [
        "https://httpbin.org/json",  # Нормальный JSON
        "https://httpbin.org/status/204", # Пустой ответ
        "https://httpbin.org/status/500",  # Ошибка 500
        "https://httpbin.org/html", # HTML
    ]

    for url in urls:
        print(f"URL: {url}")
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        try:
            data = response.json()
            print(f"JSON data: {data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Ошибка декодирования JSON. Текст ответа: {response.text}") # Выводим первые 100 символов
        except Exception as e:
            print(f"Другая ошибка: {e}")
        print("-" * 20)


    print("\nПример запроса без обработки ошибок (204 No Content):")
    response = requests.get("https://httpbin.org/status/204")
    print("Статус:", response.status_code)
    try:
        # Здесь возникнет исключение, потому что json() не сможет распарсить пустой ответ
        data = response.json()
        print("Результат:", data)
    except requests.exceptions.JSONDecodeError:
        print(f"Ошибка декодирования JSON. Текст ответа: {response.text}")