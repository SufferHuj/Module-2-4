# 1
# has_ticket = True
# has_passport = False
#
# can_board_place = has_ticket and has_passport
# print(can_board_place)

#3
# num_1 = int(input("Введи первое число: "))
# num_2 = int(input("Введи первое число: "))
#
# if num_1 > 10 and num_2 > 10:
#     print("Число не может быть > 10")
# else:
#     print("Твоё число в диапазоне")

#4
# is_raining = True
# has_umbrella = False
#
# can_go_umbrella = is_raining or has_umbrella
# print(can_go_umbrella)

#5
# is_hungry = False
# has_snack = False
#
# can_eat_now = is_hungry or has_snack
# print(can_eat_now)

#6
# num_1 = int(input("Введи первое число: "))
# num_2 = int(input("Введи первое число: "))
#
# if num_1 > 50 or num_2 < 30:
#     print("Невалидный результат")
# else:
#     print("Результат валидный")

#7
# is_logged_in = False
# need_login = not is_logged_in
#
# print(need_login)

#8
# is_empty = True
# has_items = not is_empty
# print(has_items)

#9
# 1. Создание переменных
# password1 = "123"
# password2 = "123"
#
# assert password2 == password1, "Строки НЕ совпадают"
#
# print("Строки совпадают")

#10
# x = 1
# y = True
#
# print(x == y)

#11
# n1 = 777
# n2 = 775
#
# assert n1 != n2, "Числа РАВНЫ"
#
# print("Числа не равны")

#12
# n = 1
# print(n != False)

# опционально 1.1
# text = "Hello, Python!"
#
# print(text[3:-4])

# опционально 1.2
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(alphabet[:10])
# print(alphabet[-5:])
# print(alphabet[::2])

# опцинально 1.3
# reversed_text = "text"
# print(reversed_text[::-1])

# опционально 2.1
# text = "hElLo, PyThOn!"
# text_lower = text.lower()
# text_upper = text.upper()
# print(text_lower)
# print(text_upper)

# опционально 2.2
# sentence = "this is a test sentence."
# sentence_cap = sentence.capitalize()
# sentence_title = sentence.title()
# print(sentence_cap, sentence_title)

# опционально 2.3
# mixed_case = "PYTHON programming IS Fun"
# print(mixed_case.lower())
# print(mixed_case.upper())
# print(mixed_case.capitalize())

# опционально 3.-
# phrase = "The quick brown fox jumps over the lazy dog"
# contains_fox = "fox" in phrase
# print(contains_fox)

# greeting = "Hello, world!"
# starts_with_hello = greeting.startswith("Hello")
# ends_with_world = greeting.endswith("world!")
# print(starts_with_hello, ends_with_world)

# text = "12345"
# is_digits = text.isdigit()
# text_2 = "abc123"
# is_digits_2 = text_2.isdigit()
# print(is_digits, is_digits_2)

# mixed_text = "Hello123"
# is_alphanumeric = mixed_text.isalnum()
# print(is_alphanumeric)

# whitespace_text = " "
# is_space = whitespace_text.isspace()
# print(is_space)

# опционально 4.-

# sentence = "Кот сидит на крыше."
# new_sentence = sentence.replace("Кот", "Пёс")
# print(new_sentence)
#
# phrase = "Я люблю яблоки и яблоки - самые вкусные фрукты."
# new_word_phrase = phrase.replace("яблоки", "бананы", 1)
# new_phrase = phrase.replace("яблоки", "бананы")
# print(new_word_phrase, new_phrase)
#
# text = "Привет, мир! Привет, люди! Привет, солнце!"
# print(text.replace("Привет", "Здравствуйте"))
# greeting = text.replace("люди", "друзья")
# print(greeting)

# опционально 5.-

# greeting = "   Добрый день!   "
# print(greeting.strip())
# print(greeting.lstrip())
# print(greeting.rstrip())

# опционально 6.-

# sentence = "Python - это весело!"
# words = sentence.split()
# print(words)
# rejoined_sentence = " ".join(words)
# print(rejoined_sentence)
#
# data = "яблоко,банан,вишня,груша"
# fruits = data.split(",")
# print(fruits)
# fruit_list = ". ".join(fruits)
# print(fruit_list)
#
# path = "home/user/documents/python/lesson1"
# directories = path.split('/')
# print(directories)
# windows_path = "//".join(directories)
# print(windows_path)

# опционально 7.-

name = "Дмитрий"
age = 28
print(f"Моё имя {name} и мне {age}")

city = "Москва"
t = 15.5
weather_format = "Погода в городе {} сейчас {}".format(city, t)
print(weather_format)

product = "ноутбук"
price = 54999
product_info_percent = "Товар: %s, цена: %d" % (product, price)
print(product_info_percent)





