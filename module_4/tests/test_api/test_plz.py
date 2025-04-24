import requests

def test_plz():
    s = requests.Session()
    s.headers.update({'User-Agent': 'My Custom Bot'}) # Постоянный заголовок
    s.auth = ('user', 'password') # Постоянная аутентификация

    response = s.get('https://httpbin.org/headers')
    print(response.json())

    response2 = s.post('https://httpbin.org/post', json={"data": "test"})
    print(response2.json())


def test_post_request():
    x = requests.session()

    response_1 = x.get('https://httpbin.org/cookies', cookies = {"fron-my" : "browser"})
    print(response_1.text)

    response_2 = x.get('https://httpbin.org/cookies')
    print(response_2.json())


# import requests
# import time
#
# def test_speed():
#     url = "https://httpbin.org/get"
#     num_requests = 10
#
#     print("Запросы с использованием сессии:")
#     start_time = time.time()
#
#     session = requests.Session()  # Создаем сессию
#
#     try:
#
#         for i in range(num_requests):
#
#             response = session.get(url)
#             response.raise_for_status()
#
#     except Exception as e:
#         print(f"ошибка: {e}")
#
#     finally:
#         session.close()  # закрываем сессию
#
#     end_time = time.time()
#     print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")
#
#     # Запросы БЕЗ использования сессии:
#     print("Запросы БЕЗ использования сессии:")
#     start_time = time.time()
#
#     try:
#
#         for i in range(num_requests):
#
#             response = requests.get(url)
#             response.raise_for_status()
#
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
#     end_time = time.time()
#     print(f"Время выполнения без сессии: {end_time - start_time:.4f} секунд")