# num = 1
# num +=1
# num -=2
#
# print(num)

# float_num = 12.99
# int_num = int(float_num)
# print(int_num)
#
# string_num = "45"
# conversed_num = int(string_num)
# print(type(conversed_num))
#
# invalid_string = "hello123"
# print(int(invalid_string)) # ValueError: invalid literal for int() with base 10: 'hello123'

# base = 5
# ex = 3
# result = pow(base, ex)
# print(result)
#
# num = 10
# power_result = pow(num, 4)
# print(power_result)
#
# a = 2
# b = 8
# print(pow(a, b))

# num1 = 10
# num2 = 20
# num3 = 5
# max_value = max(num1, num2, num3)
# print(max_value)
#
# num1 = 23
# num2 = 42
# num3 = 5
# num4 = 7
# mix_value = min(num4, num2, num3, num1)
# print(mix_value)
#
# numbers = [3, 8, 1, 25, 19, 4, 7]
# max_n = max(numbers)
# min_n = min(numbers)
# print(max_n, min_n)

# x = 25
# y = 4
# q = x // y
# r = x % 4
# print(q, r)
#
# a = 47
# b = 5
# d = a // 5
# l = 47 % 5
# print(d, l)

# num1 = 789
# new_num1 = len(str(num1))
# print(new_num1)
#
# large_number = 1234567890123
# print(len(str(large_number)))
#
# phone_number = 84951234567
# print(len(str(phone_number)))

# value = 3.14159
# print(round(value, 2))
#
# price = 19.999
# print(round(price))
#
# grades = [89.9, 92.75, 88.6, 91.3]
# r_g = [round(grade, 1) for grade in grades]
# print(r_g)

# import math
#
# price = 19.99
# p_down = math.floor(price)
# p_up = math.ceil(price)
# print(p_down,p_up)
#
# height = 175.45
# print(math.floor(height), math.ceil(height))

# num1 = 10.0
# num2 = 10.5
# print(num1.is_integer(), num2.is_integer())
#
# num = float(input("Введите число: "))
#
# if num.is_integer():
#     print(f"Число: {num} является целым")
# else:
#     print(f"Число: {num} не является целым")

# small_num = 5.67e-5
#
# # Вывод числа в научном формате
# print("Научный формат:", small_num)
#
# # Вывод числа в фиксированном формате с 8 знаками после запятой
# print("Фиксированный формат: {:.8f}".format(small_num))

# username = None
# if username is None:
#     print("Гость")
#
# def greet_user(name):
#
#     if name is None:
#         print("Аноним")
#     else:
#         print(f"Привет, {name}")
#
# greet_user(None)
# greet_user("Vadim")
#
# user_info = {
#     "name": "Vadim",
#     "age": 17,
#     "email": None
# }
#
# if user_info["email"] is None:
#     user_info["email"] = "не указан"
#
# print(user_info)

# def calculate_discount(price, discount=None):
#
#     if discount is None:
#         discount = 0.05
#     d_price = price * (1 - discount)
#     return d_price
#
# my_p = calculate_discount(500)
# print(my_p)
#
# def add_to_list(item, my_list=None):
#
#     if my_list is None:
#         my_list = []
#
#     my_list.append(item)
#     return my_list # Возвращаем обновлённый список
#
#
# print(add_to_list(3))
# print(add_to_list(66))
# print(add_to_list(777))

car = "BWM"  # Шаг 1: переменная со значением None

# Шаг 2 и 3: проверяем и выводим соответствующее сообщение
if car is not None:
    print(car)
else:
    print("Автомобиль не указан")