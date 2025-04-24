# # # from typing import final
# # #
# # # NewValue = "ПОД"
# # # new_value = "ЗАЛУПНЫЙ ТВОРОЖОК"
# # # OldValue = f"твоё имя: {NewValue}{new_value}"
# # #
# # # #print(OldValue)
# # #
# # # new_value = "ДУБНЫЙ"
# # # OldValue = f"твоё имя: {NewValue}{new_value}"
# # #
# # # #print(OldValue)
# # #
# # # #num_1 = int(input("Писка твоя размером: "))
# # # #num_2 = int(input("Очко с размером: "))
# # #
# # # #look_on_your_ass = num_1 >= 10 or num_2 <5
# # #
# # # #print("your ass: ", look_on_your_ass)
# # #
# # # is_empty = True
# # # has_items = 1
# # #
# # # #print(is_empty == has_items)
# # #
# # # name = "Dima"
# # # age = 28
# # # greet = f"{name} : {28}"
# # #
# # # #print(greet)
# # #
# # # a = 2
# # # b = 8
# # # c = pow(a, b)
# # # #print(c)
# # #
# # # phone_number = 84951234567
# # # new_number = len(str(phone_number))
# # # #print(new_number)
# # #
# # # #num = float(input("Invalid number: "))
# # #
# # # #if num.is_integer():
# # # #   print("Full number")
# # # #else:
# # # #    print("Number wrong")
# # #
# # # #username = None
# # #
# # # #if username is None:
# # # #   print("Гость")
# # #
# # # def greet_user(name=None):
# # #     if name is None:
# # #         name = "Аноним"
# # #     print(f"Привет, {name}!")
# # #
# # # greet_user(None)
# # # greet_user("Ivan")
# # #
# # # user_info = {"name":21, "age":33, "email":None}
# # # if user_info["email"] is None:
# # #     user_info["email"] = "не указано"
# # #
# # # print(user_info)
# # #
# # # def calculate_discount(price, discount=None):
# # #     if discount is None:
# # #         discount = 0.05
# # #
# # #     final_price = price * (1 - discount)
# # #     return final_price
# # #
# # # print(calculate_discount(100))
# # # print(round(calculate_discount(105)))
# # #
# # #
# # # def title(book = None):
# # #     if book is not None:
# # #         print(book)
# # #     else:
# # #         print("Book not find")
# # #
# # # title("Harry Potter")
# # #
# # # n = [1, 2, "zalupa", True, 1.22]
# # # n.append(666)
# # #
# # #
# # # n.insert(0, "HUYLO")
# # #
# # #
# # # n.extend(["two hundred dicks", 9.9])
# # # print(n)
# # #
# # # a = n.index(True)
# # # print(a)
# # #
# # # n.remove("two hundred dicks")
# # # print(n)
# # #
# # # numbers = [10,20,40,50]
# # # numbers.insert(2, 30)
# # # print(numbers)
# # #
# # # numbers.clear()
# # # print(numbers)
# # #
# # # a = [1, 2, 3]
# # # b = [4, 5, 6]
# # #
# # # c = a + b
# # # print(c)
# # #
# # # assert len(c) == len(a) + len(b)
# # # print("Все работает правильно!")
# # #
# # #
# # # users = {
# # #     "Alice": {
# # #         "phone": "+971478745",
# # #         "email": "alice12@gmail.com"
# # #     },
# # #     "Bob": {
# # #         "phone": "+876390444",
# # #         "email": "bob@gmail.com",
# # #         "skype": "bob123"
# # #     }
# # # }
# # #
# # # users_new = {"Vadim": {"phone": "+79994342321", "email": "test@gmail.com"}}
# # #
# # # users.update(users_new)
# # # users["Vadim"]["phone"] = "+7999***3222"
# # #
# # #
# # # residence = {
# # #     "residence": {
# # #         "country": "Thailand",
# # #         "city": "Phuket",
# # #         "district": "Thalang"
# # #     }
# # # }
# # #
# # # users.update(residence)
# # # users["Vadim"].update(users["residence"])
# # # del users["residence"]
# # # print(users)
# # #
# # # print(users["Vadim"]["country"])
# # #
# # # n = (1, 2, "ass", {"name": "suka"})
# # #
# # # n2 = tuple(n)
# # #
# # # assert n == n2
# # #
# # # print(n2)
# # #
# # # tuple1 = (231, {"object": "in_tuple"}, 2)
# # # tuple2 = tuple(tuple1)
# # # assert tuple1 == tuple2
# # # print(tuple1 == tuple2)  # Вывод: True
# # #
# # # print(len(tuple1))
# #
# #
# # new = (3, 12, 1, 3, 20, 123, 3, 32423, 3, {"object": "in_tuple"}, 3, 232)
# #
# # p = new[5]
# #
# #
# #
# #
# # n = ("apple", "banana", "cherry", "apple")
# #
# # n_1 = n.index("apple")
# # n_2 = n.count("apple")
# # a, b, *rest = n
# # tuple_2 = tuple(rest)
# #
# # print(tuple_2)
# #
# # assert len(tuple_2) == 2, f"Ожидаемая длина = 2, получено: {len(tuple_2)}"
# #
# # n = {1, 2, "name", ("sex", "yes")}
# #
# # print(n)
#
#
# m = {1, 1.2, 11, "zalupa", 4, 3242}
# m.add(4343)
#
# n = {"1", 11, 3, 4, "russia"}
#
# x = m == n
#
# print(x)
#
# s1 = [10, 20, 30, 40, 50]
# s2 = [20, 25, 30, 35, 40]
#
# x1 = set(s1)
# x2 = set(s2)
#
# x3 = x1.difference(x2)
#
# print(x3)
#
# x4 = x1 ^ x2
#
# x = range(6,2,-2)
# x1 = list(x)
# print(x1)

# print('значение h: ', ord("h"))
# print('значение H: ', ord("H"))

# text = "Hello world !!!"
# arr = ["10", 20, 30, 40, 50]
# tpl = (1, 2, 3, 4, 5)
# st = {100, 200, 300, 400, 500}
# lst = {"apple" : "aaa", "juice": {"banana": True, "cherry": 25, "date": "dfs"}}

# num = 0
#
# if num % 2 == 0 and num > 0:
#     print(f"Число: {num} чётное и положительное")
# elif num % 2 == 0 and num < 0:
#     print(f"Число: {num} чётное и отрицательное")
# elif num % 2 != 0 and num > 0:
#     print(f"Число: {num} нечётное и положительное")
# elif num % 2 != 0 and num < 0:
#     print(f"Число: {num} нечётное и отрицательное")
# else:
#     print(f"Число: {num} равно нулю")

# num_1 = 100
# num_2 = 100

# if num_1 > num_2:
#     print(f"Число {num_1} максимальное")
# elif num_1 < num_2:
#     print(f"Число {num_2} максимальное")
# else:
#     print(f"Числа равны")

# if num_1 == num_2:
#     print(f"Числа равны")
# else:
#     max_num = max(num_1, num_2)
#     print(f"Число {max_num} максимальное")

# used_logins = ["user123", "hacker", "test_bot"]
#
# new_login = "user1234"
#
# if new_login in used_logins:
#     print(f"Логин {new_login} есть в системе")
# else:
#     print(f"Логина {new_login} нет в системе")

# unique_numbers = (1, 2, 3, 4, 5)
# for number in unique_numbers:
#     print("Число из кортежа:", number)

# n = [10, 20, 30, 40, 50]
#
# for n in n:
#     print("Число №", n)

# name = "Hello, Python!"
#
# for word in name:
#     print(word)

# name_friend_and_age = {"Petr": 37, "Ivan": 20, "Zalupa": 77, "Stas": 8}
#
# for name, age in name_friend_and_age.items():
#     print(f"Имя друга: {name}, его возраст: {age}")
#     print("Имя:", name, "возраст:", age)

# num = 10
#
# while num >= 1:
#     print(f"Номер числа = {num}")
#     num -= 1
#
# print("Цикл завершён!")

# while True:
#     password = input("Введите Ваш пароль: ")
#
#     if password in password == "123x45":
#         print("Доступ разрешен!")
#         break
#     else:
#         print("Вы ввели неверный пароль")

# num = 10
#
# while num > 0:
#     if num % 2 != 0:
#         print(num)
#     num = num - 1

# countdown = 5
# while countdown > 0:
#     print("Обратный отсчёт:", countdown)
#     countdown -= 1  # Уменьшаем значение
# print("Поехали!")

# arr = [10, 20, 53, 40, 50, 70]
#
# for number in arr:
#     print(number ** 2)

# day = int(input("Введи цифру от 1 до 7 и узнай какой сейчас день недели: "))
#
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day in [6, 7]:
#     print("Выходной")
# elif day > 7 or day < 1:
#     print("Введи цифру от 1 до 7")
# else:
#     print("Сегодня рабочий день, браток")
#
# for n in range(1,21):
#     if n % 3 == 0:
#         continue
#     print(n)

# n = 1  # Начинаем с 1
# #
# while n <= 20:  # Пока число не больше 20
#     if n % 3 == 0:  # Если число кратно 3
#         n += 1  # Увеличиваем число и пропускаем итерацию
#         continue  # Пропускаем оставшуюся часть кода
#
#     print(n)  # Выводим число, если оно не кратно 3
#     n += 1  # Переходим к следующему числу

# print("Имя     \t\tДолжность   \t\tЗарплата")
# print("Иванов  \t\tМенеджер    \t\t50000")
# print("Петров  \t\tПрограммист \t\t70000")

# products = {
#     "Яблоки": 100,
#     "Бананы": 80,
#     "Молоко": 120,
#     "Хлеб": 50,
#     "Сыр": 300
# }
#
# print("Продукт\t\tЦена (руб)")
# print("-" * 25)
#
# for product, price in products.items():
#     print(f"{product.ljust(10)}\t{price}")

# for num in range(1, 6):
#     for x in range(1, 6):
#         print(f"{num} + {x} = {num + x}", end="\t")
#     print()

# print("ТАБЛИЦА УМНОЖЕНИЯ\n")
# # Внешний цикл по числам от 1 до 10
# for i in range(1, 11):
#     # Вложенный цикл для умножения каждого числа на числа от 1 до 10
#     for j in range(1, 11):
#         print(f"{i:2} * {j:2} = {i * j:2}", end="\t")  # Результаты отображаются в строку
#     print()  # Переход на новую строку после внутреннего цикла

# numbers = [10, 0, 5, "abc", 2]
#
# for number in numbers:
#     try:
#         result = 100 / number
#         print(f"Результат = {result}")
#
#     except ZeroDivisionError:
#         print("Ошибка. Деление на ноль невозможно.")
#
#     except TypeError:
#         print("Ошибка. Неверный тип данных")

# x = ["123", "text", None, "213md", "456"]
#
# for x in x:
#     try:
#         result = int(x)
#         print(f"Число = {result}")
#
#     except (ValueError, TypeError):
#         print(f"Ошибка. Преобразовать в число {x} нельзя")

# data = [ (10, 5), (3, 0), (7, "str") ]
#
# for a, b in data:
#     try:
#         result = a / b
#         print(f"Результат = {result}")
#
#     except ZeroDivisionError:
#         print(f"Ошибка. Деление на {b} недопустимо")
#
#     except TypeError:
#         print(f"Ошибка. Невалидный тип данных {b}")

#1 арифметическое/среднее
# num_1 = 100
# num_2 = 111
# num_3 = 211
#
# print(num_1 + num_2 == num_3)
# print(num_1 * num_2 < num_3)

#1 логическое/среднее
# n = int(input("Введи цифру от 10 до 20: "))
#
# if 10 <= n <= 20:
#     print(f"Твоя цифра {n} входит в диапазон")
# else:
#     print("Цифра вне диапазона")

#1 арифметическое/сложное

# try:
#     n_1 = float(input("Введи первое число: "))
#     n_2 = float(input("Введи второе число: "))
#     operation = input("Введи операцию (+, -, *, /, %, //, **): ")
#
#     if operation in ["/", "%", "//"] and n_2 == 0:
#         print("Ошибка. Деление на 0 невозможно")
#
#     elif operation == "+":
#         print("Результат: ", n_1 + n_2)
#
#     elif operation == "-":
#         print("Результат: ", n_1 - n_2)
#
#     elif operation == "*":
#         print("Результат: ", n_1 * n_2)
#
#     elif operation == "/":
#         print("Результат: ", n_1 / n_2)
#
#     elif operation == "%":
#         print("Результат: ", n_1 % n_2)
#
#     elif operation == "//":
#         print("Результат: ", n_1 // n_2)
#
#     elif operation == "**":
#         print("Результат: ", n_1 ** n_2)
#
#     else:
#         print("Ошибка. Введите корректный оператор!")
#
# except ValueError:
#     print("Ошибка. Введите числовое значение!")

#2/1 простое
# text = "Python is awesome!"
# print(text.upper())
# print(text.replace("awesome","amazing"))
#2/2
# text = "Hello, Python!"
# print(text[:5])
# print(text[::2])
#2/3
# pi = 3.14159
# print(round(pi, 2))

# user = None
#
# # Проверка перед доступом к атрибуту
# if user is not None:
#     print(user.name)
# else:
#     print("Объект user не инициализирован")

#2/1 средний

# quote = "Python is easy and powerful!"
#
# new_quote = quote.replace("easy", "fun").replace("powerful!", "versalite")
# print(new_quote)

#2/2 средний

# name = "Alice"
# age = 25
#
# print(f"{name} is {age} years old")

#2/1 сложное

# data = "Price: 1234.5678 USD"
#
# num = float(data[7:-4])
# new_int = round(num, 2)
# print(f"Rounded price: {new_int} USD")

#3/1 простое

# fruits = ["apple", "banana", "cherry", "date"]
#
# fruits.insert(2,"kiwi")
# fruits.remove("banana")
# print(fruits)

#3/2 простое

# person = {"name": "Alice", "age": 25, "city": "New York"}
#
# person["age"] = 26
# person["profession"] = "engineer"
# print(person)

#3/1 среднее

# numbers = (10, 20, 30, 40, 50)
# print(numbers[1])

#3/2 среднее

# colors = {"red", "blue", "green"}
# colors.add("yellow")
# colors.remove("blue")
# colors.add("red")
# print(colors)

#3/1 сложное

#1 способ
# numbers = list(range(1, 21))
# numbers_len = sum(numbers)
# number_3 = [n for n in numbers if n % 3 == 0]
#
# print("Список диапазона чисел: ", numbers)
# print("Сумма всех чисел: ", numbers_len)
# print(f"Числа при деление на 3: {number_3}")

# 2 способ
# numbers = list(range(1, 21))
# # numbers_sum = sum(numbers)
# numbers_2 = []
# #
# for n in numbers:
#     if n % 3 == 0:
#         numbers_2.append(n)
# # print(numbers)
# # print(numbers_sum)
# print(numbers_2)

#4 / простое
# for i in range(1, 11):
#     print(i)

#4 /среднее
# n = 10
# while n > 0:
#     print("Число: ", n)
#     n -= 1
# print("Счёт завершён!")

# n = 20
#
# while n > 0:
#     print("Число: ", n)
#     n -= 2
# print("Обратный отсчёт завершён")

# for n in range(20, 0, -2):
#     print("Number: ", n)
# print("END!!!")

#4 /сложно

# for n in range(1, 11):
#     print(f"5 * {n} = {5 * n}", end = "\t")

#1
# for n in range(1, 11):
#     result = n * 7
#     print(f"{n} * 7 = {result}", end = "\t")
#2
# for i in range(1, 6):
#     for j in range(2, 4):
#         print(f"{i} ** {j} = {i ** j}", end="\t")


# items = {
#     "Healing Potion": 100,
#     "Mana Potion": 80,
#     "Scroll of Speed": 150,
#     "Magic Artifact": 300
# }
#
# name_item = input("Enter name item: ")
#
#
# if name_item in items:
#     try:
#         quantity_item = int(input("Enter quantity item: "))
#
#         total_price = items[name_item] * quantity_item
#         print(f"Стоимость товара: {total_price}")
#
#         if total_price > 500:
#             total_price *= 0.8
#             print(f"Стоимость товара c учётом скидки: {total_price}")
#
#     except ValueError:
#         print("Ввведи правильное количество товара")
# else:
#     print("У меня такого нет, попробуй в другом месте!")


# 1 сложное
# print("Калькулятор чисел\t")
# print("---" * 10)
#
# try:
#     n_1 = float(input("Введи первое число: "))
#     n_2 = float(input("Введи второе число: "))
#     operation = input("Выбери одну из арифметических операций (+, -, /, %, //, *): ")
#
#     if operation in ["/", "//", "%"] and n_2 == 0:
#         print("Ошибка. Деление на 0 невозможно")
#
#     elif operation == "+":
#         print("Результат: ", n_1 + n_2)
#
#     elif operation == "-":
#         print(f"Результат: {n_1 - n_2}")
#
#     elif operation == "/":
#         print("Результат: ", n_1 / n_2)
#
#     elif operation == "*":
#         print(f"Результат: {n_1 * n_2}")
#
#     elif operation == "//":
#         print("Результат: ", n_1 // n_2)
#
#     elif operation == "%":
#         print(f"Результат: {n_1 * n_2}")
#
#     else:
#         print("Ошибка. Выбери верную арифметическую операцию")
#
# except ValueError:
#     print("Ошибка. Введи числовое значение")

# data = "Price: 1234.5678 USD"
#
# number = float(data[7:16])
# number_1 = round(number, 2)
#
# print(f"Rounded price: {number_1} USD")

# x = list(range(1, 21))
#
# x_sum = sum(x)
#
# x_3 = [n for n in x if n % 3 == 0]
#
# print(f"Оба списка выглядят так: {x} и {x_3}")

# for num in range(1, 11):
#     print(num)

# n = 10
#
# while n > 0:
#     print("Число: ", n)
#     n -= 1
#
# print("Счёт завершён")
#
# numbers = list(range(10, 1, -1)) # Создаём список чисел от 10 до 1
# index = 0 # Индекс для перебора списка
#
# while index < len(numbers):
#     print("Число: ", numbers[index])
#     index += 1 # Переход к следующему элементу
# print("Счёт закончен")
#
# for x in range(1, 2):
#     for y in range(1, 11):
#         print(f"{y} * 5 = {y * 5}", end = "   ")
#     print()
#
# for i in range(1, 11):
#     result = 5 * i
#     print(f"5 * {i} = {result}", end = "   ")


# my_items = {
#     "Зелье лечения": 100,
#     "Зелье маны": 80,
#     "Свиток скорости": 150,
#     "Артефакт магии": 300
# }
#
# name_item = input("В моей лавке есть приправки! Зелье лечения, Зелье маны, Свиток скорости, Артефакт магии. Какой товар ищешь, путник?: ")
#
# try:
#     if name_item in my_items:
#
#         q_items = int(input("Какое количество?: "))
#
#         result = my_items[name_item] * q_items
#         print("Сегодня цена:", result)
#
#         if result > 500:
#             result = result * 0.8
#             print(f"Но тебе повезло, отдам со скидкой!")
#
#         print(f"Моя цена с учётом скидки: {result}")
#
#     else:
#         print("У меня такого нет, попробуй в другом месте!")
#
# except ValueError:
#     print("Не понял, сколько ты хочешь?")