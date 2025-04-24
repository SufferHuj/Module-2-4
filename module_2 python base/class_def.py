# def greet():
#     print("Hello, world!")
#
# greet()

# def greet_user(name):
#     print(f"Привет {name}!")
#
# greet_user("Ivan")
# greet_user("Maria")

# def sum_numbers(a, b):
#     sum_numbers = a + b
#     print(f"Сумма чисел = {sum_numbers}")
#
# sum_numbers(5, 3)
# sum_numbers(-1, 10)

# def is_even(number):
#     if number % 2 == 0:
#         print(f"Число: {number} чётное")
#     else:
#         print("Число:", number, "нечётное")
#
# is_even(4)
# is_even(7)
# is_even(0)

# def rectangle_area(width, height):
#     if width <= 0 or height <= 0:
#         print("Некорректные значения")
#     else:
#         area = width * height
#         print(f"Площадь прямоугольника = {area}")
#
# rectangle_area(5, 10)
# rectangle_area(-2, 5)
# rectangle_area(5, -2)
# rectangle_area(0, 10)

# def greet_person(name, age):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
# greet_person("John", 99)
# greet_person(name = "Petr", age = 77)

# def circle_area(r, pi = 3.14159):
#     circle = pi * r ** 2
#     print("Площадь круга = ", circle)
#
# circle_area(2)
# circle_area(r = 2, pi = 3.14)

# def book_info(title = "Неизвестно", author = "Неизвестно", year = "Неизвестно", genre = "Неизвестно"):
#     print(f"Название: {title}, Автор: {author}, Год: {year}, Жанр: {genre}")
#
# book_info("Горе от ума", "Достоевский", 1927, "Роман")
# book_info(genre= "Боевик", title= "Залечь в говно в Брюгге", author= "Данцова", year= 999)
# book_info("Кто есть бог? Если не я", "Каное Квест", 666)

# def convert_currency(amount, rate, from_currency="USD", to_currency="EUR"):
#     currency = amount * rate
#
#     if from_currency == "USD" and to_currency == "EUR":
#         print("Курс обмена USD на EUR = ", currency)
#
#     elif from_currency == "RUB" and to_currency == "USD":
#         print("Курс обмена RUB на USD = ", currency)
#
#     else:
#         print(f"Курс обмена {from_currency} на {to_currency} = {currency}")
#
# convert_currency(1001, 2)
# convert_currency(1003, 83, "RUB", "USD")
# convert_currency(rate = 83000, amount= 2, from_currency= "BTC", to_currency= "USD")

# def convert_currency(amount, rate, from_currency="USD", to_currency="EUR"):
#     return amount * rate
#
# print(convert_currency(1001, 2))
# print(convert_currency(1003, 83, "RUB", "USD"))
# print(convert_currency(rate = 83000, amount= 2, from_currency= "BTC", to_currency= "USD"))

# def max_of_two(a, b):
#     return max(a, b)
#
# print(max_of_two(5, 10))
# print(max_of_two(15, 3))
# print(max_of_two(-1, -5))

# def string_length(s):
#     return len(s)
#
# print(string_length("Hello"))
# print(string_length("Python is fun"))
# print(string_length(""))

# функции практика задание 1

# def calculate_delivery_cost(weight, distance, fragile=False):
#
#     base_cost = 10 * weight + 5 * distance
#
#     if fragile:
#         base_cost *= 1.5
#
#     base_cost = max(200, base_cost)
#
#     return base_cost
#
# print("Стоимость доставки =", calculate_delivery_cost(1, 100), "руб")
# print("Стоимость доставки =", int(calculate_delivery_cost(1, 100, True)), "руб")
# print("Стоимость доставки =", calculate_delivery_cost(1, 10), "руб")

# функции практика задание 2

# def analyze_numbers(numbers):
#
#     if not numbers:
#         return {
#             "average": None,
#             "min": None,
#             "max": None,
#             "even_count": None
#                 }
#
#     average = sum(numbers) / len(numbers)
#     minimal = min(numbers)
#     maximal = max(numbers)
#     even_count = len([n for n in numbers if n % 2 == 0]) # альтернатива sum(1 for n in numbers if n % 2 == 0)
#                                                                         # for n in numbers — перебираем все элементы списка
#                                                                         # if n % 2 == 0 — берём только чётные числа
#                                                                         # 1 for ... — за каждое чётное число добавляем единицу
#                                                                         # sum(...) — суммируем все эти единицы → получаем количество чётных чисел.
#     return {
#         "average": average,
#         "min": minimal,
#         "max": maximal,
#         "even_count": even_count
#     }
#
# print(analyze_numbers([1, 332, 21, 333, 1000]))

# функции практика задание 3

# def filter_list(data, threshold):
#     data_new = []
#
#     for n in data:
#         if n >= threshold:
#             data_new.append(n)
#     return data_new
#
# result = filter_list(data=[1, 5, 10, 2, 8, 12], threshold = 7)
#
# print(result)

# def filter_list(data, threshold):
#     return [n for n in data if n >= threshold]
#
# print(filter_list(data=[1, 5, 10, 2, 8, 12], threshold = 7))








# задача 1

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         print(f"Книга: {self.title}, автор: {self.author}, страниц в книге: {self.pages}")
#
# book_1 = Book("Горе от ума", "Достоевский", 777)
#
# book_1.title = "Идиот"
# book_1.author = "Грибоедов"
# print(f"Книга: {book_1.title}, автор: {book_1.author}, страниц в книге: {book_1.pages}")
#
# book_1.genre = "Роман"
# print(book_1.title, book_1.author, book_1.pages, book_1.genre)

# задача 2

# class Person:
#     name = "Undefined"
#
#     def print_name(self):
#         print(self.name)
#
# tom = Person()
#
# tom.name = "Ivan"
# tom.print_name()

# задача 3

# class Animal:
#     name = "Tarzan"
#     age = 31
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print(f"I am an animal, my name is {self.name} and my age {self.age}")
#
# animal_o = Animal("Ivan", 77)
#
#
# animal_o.name = "Sancho"
# animal_o.age = 66
# animal_o.speak()

# задача 4

# class Numbers:
#
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2
#
#     def num(self):
#         max_num = max(self.number_1, self.number_2)
#         print("Максимальное число:", max_num)
#
#         if max_num % 2 == 0:
#             print(f"Число {max_num} чётное")
#         else:
#             print(f"Число {max_num} не чётное")
#
#         if max_num > 0:
#             print(f"Число {max_num} положительное")
#         elif max_num < 0:
#             print(f"Число {max_num} отрицательное")
#         else:
#             print(f"Число {max_num} это ноль")
#
# max_number = Numbers(-20, 0)
# max_number.num()


# задача 5 от gpt

# class Numbers:
#
#     def __init__(self, num1, num2, num3):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#
#     def analyze(self):
#
#         average_num = round((self.num1 + self.num2 + self.num3) / 3)
#
#         print("Среднее арифметическое:", average_num)
#
#         if average_num > self.num1 and average_num > self.num2 and average_num > self.num3:
#             print(f"Среднее арифметическое {average_num} больше каждого из трёх чисел")
#         else:
#             print(f"Среднее арифметическое {average_num} меньше хотя бы одного из чисел")
#
#         if average_num % 3 == 0:
#             print(f"Среднее арифметическое {average_num} делится на 3")
#         else:
#             print(f"Среднее арифметическое {average_num} не делиться на 3")
#
# my_number = Numbers(300, 2222, 6666)
# my_number.analyze()

# задание из наследования

#Базовый класс Account моделирует обычный банковский счёт
# class Account:
#     def __init__(self, name, balance):
#         # Сохраняем имя владельца и начальный баланс
#         self.name = name
#         self.balance = balance
#
#         # Если баланс отрицательный — выбрасываем ошибку
#         if balance < 0:
#             raise ValueError(f"{self.balance} не может быть отрицательным")
#
#     def deposit(self, amount):
#         # Метод для внесения денег на счёт
#         self.balance += amount
#
#     def withdraw(self, amount):
#         # Метод для снятия денег со счёта
#         # Проверка: нельзя снимать больше, чем есть
#         if amount > self.balance:
#             raise ValueError(f"{self.balance} не может быть отрицательным")
#         self.balance -= amount
#
# # Класс SavingsAccount — дочерний от Account, моделирует сберегательный счёт
# class SavingsAccount(Account):
#     def __init__(self, name, balance, interest_rate):
#         # Вызываем родительский __init__ для установки имени и баланса
#         super().__init__(name, balance)
#         # Добавляем дополнительное поле: процент на остаток
#         self.interest_rate = interest_rate
#
#     def withdraw(self, amount):
#         # Переопределяем метод снятия
#         # Проверка: после снятия должно оставаться не меньше 100
#         if self.balance - amount < 100:
#             raise ValueError(f"Баланс: {self.balance}. Нельзя снимать — должен оставаться минимум 100 на счёте")
#
#         # Если условие прошло — вызываем родительский метод снятия
#         super().withdraw(amount)
#         print("Остаток:", self.balance)
#
# # Пример использования класса:
# # Создаём объект сберегательного счёта с именем, балансом и процентом на остаток
# my_account = SavingsAccount("Ivan Ivanov", 100000, 25)
#
# # Пример пополнения счёта
# my_account.deposit(10000)
# # Пример снятия со счёта
# my_account.withdraw(109900)
#
# # Печатаем основные данные: имя владельца, баланс и процент
# print(my_account.name, my_account.balance, my_account.interest_rate)

# задание 1 реестр животных (методы классов)

# class Animal:
#     species = [] # Атрибут класса — общий список всех зарегистрированных видов животных
#
#     def __init__(self, kind):
#
#         self.kind = kind # Сохраняем вид конкретного животного в атрибуте экземпляра
#         self.add_species(kind) # При создании животного вызываем метод, который добавляет вид в реестр
#
#     @classmethod # Метод помечен classmethod, чтобы он работал с самим классом (cls), а не с конкретным объектом.
#     def add_species (cls, kind):
#
#         if kind not in cls.species:
#             cls.species.append(kind) #Добавляем вид в список species, если его там ещё нет
#
#     @classmethod
#     def show_species (cls):
#         print(f"Список всех видов: {cls.species}") # Печатаем весь список зарегистрированных видов
#
# animal1 = Animal("dog") # При создании каждого животного вызывается __init__, а он вызывает add_species
# animal2 = Animal("cat")
# animal3 = Animal("elephant")
# animal4 = Animal("cat") # Второй "cat" не добавляется повторно, тк add_species проверяет уникальность
#
# Animal.show_species() # Вызываем метод отображения списка

# задание 1 реестр Конвертер валют (staticmethod)

# class CurrencyConverter:
#
#     @staticmethod
#     def usd_to_eur (amount):
#         return amount * 0.85
#
#     @staticmethod
#     def eur_to_usd (amount):
#         return amount * 1.18
#
# #print(CurrencyConverter.usd_to_eur(1000))
#
# # print(CurrencyConverter.eur_to_usd(1000))
#
# eur_c = CurrencyConverter()
# print(eur_c.usd_to_eur(1000))

# пример из раздела с одним подчеркиванием

# class BankAccount:
#
#     def __init__(self, balance):
#
#         self._balance = balance
#
#     def deposit(self, amount):
#
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Сумма депозита должна быть положительной.")
#
#     def withdraw (self, amount):
#
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#         else:
#             print("Недостаточно средств или некорректная сумма.")
#
#     def get_balance (self):
#         return self._balance
#
# account = BankAccount(100)
# account.deposit(1000)
# account.withdraw(1000)
#
# print(f"Остаток по твоему счёту: {account.get_balance()}")

# задание 1 финальное методы классов
# class Book:
#
#     def __init__(self, title, author, pages):
#
#         self._title = title
#         self._author = author
#         self._pages = pages
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, new_title):
#         self._title = new_title
#
#     @property
#     def author(self):
#         return self._author
#
#     @author.setter
#     def author(self, new_author):
#         self._author = new_author
#
#     @property
#     def pages(self):
#         return self._pages
#
#     @pages.setter
#     def pages(self, new_pages):
#
#         if new_pages < 0:
#             print("Количество страниц не может быть отрицательным")
#         else:
#             self._pages = new_pages
#
# book = Book(pages= 777, title="Мастер и Маргарита",author="Михаил Булгаков")
# book.pages = -10
# book.author = 'Вадим Новичков'
# print(book.title, book.author, book.pages)

# задание 2 финальное методы классов

# class BankAccount:
#
#     def __init__(self, account_number, balance):
#
#         self._account_number = account_number
#         self._balance = balance
#
#     @property
#     def account_number(self):
#         return self._account_number
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, amount):
#         if amount > 0:
#             self._balance += amount
#
#         else:
#             print("Операция снятия средств не поддерживается. Используйте метод withdraw()")
#
#     def withdraw(self, amount):
#
#         if amount <= 0:
#             print("Сумма должна быть положительной")
#
#         elif amount > self._balance:
#             print(f"Сумма снятия не может быть больше текущего баланса {self._balance}")
#
#         else:
#             self._balance -= amount
#             print(f"Снято: {amount}. Остаток: {self._balance}")
#
# my_BankAccount = BankAccount(12345678, 5000)
# my_BankAccount.withdraw(5001)
# print(my_BankAccount.account_number, my_BankAccount.balance)

# задание 1 из исключения
# def safe_divide(a, b):
#     try:
#         result = a / b
#         print(f"Результат деления = {result}")
#
#     except ZeroDivisionError:
#         print("Ошибка. Деление на ноль невозможно")
#     except TypeError:
#         print("Ошибка. Введите числовое значение")
#
# safe_divide(8, 2)

# задание 2 из исключения

# filename = input("Введите имя файла: ")
#
# def read_file(filename):
#
#     if not filename:
#         print("Ошибка. Имя файла не может быть пустым")
#         return
#
#     try:
#         with open(filename, "r") as f:
#             content = f.read()
#             print(content)
#
#     except FileNotFoundError:
#         print("Ошибка. Такого файла не существует")
#
# read_file(filename)

# задание 3 из исключения
# numbers_list = [1, 33, "ass", 454, 432, 555, 0]
#
# def devide_numbers(numbers_list):
#     for number in numbers_list:
#         try:
#             result = 100 / number
#             print("Результат вычисления = ", round(result, 2))
#
#         except ZeroDivisionError:
#             print("Ошибка! Деление на ноль невозможно")
#
#         except TypeError:
#             print("Ошибка! Некорректный тип данных в списке")
#
# devide_numbers(numbers_list)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book.title)
        else:
            print(f"Книга '{book.title}' уже занята.")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            status = "Занята" if book.is_borrowed else "Свободна"
            print(f"{book.title} ({book.author}) - {status}")


