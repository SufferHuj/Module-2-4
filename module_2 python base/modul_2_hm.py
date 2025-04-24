# #1.1
# n = int(input("Введи число: "))
#
# if n % 2 == 0:
#     print("Число {} чётное".format(n))
# else:
#     print(f"Число {n} нечётное")
#
# #1.2
# count_items = 3
# price_one_item = 5000
# total_price = count_items * price_one_item
#
# if total_price > 10000:
#     total_price *= 0.8
#     print("Итоговая сумма заказа с учётом 20% скидки: ", total_price)
# elif total_price > 5000:
#     total_price *= 0.9
#     print("Итоговая сумма заказа с учётом 10% скидки: ", total_price)
# else:
#     print("Итоговая сумма заказа: ", total_price)
#
# #1.3
# password = "qwerty12"
#
# if password == "qwerty123":
#     print("Доступ разрешён")
# elif password.strip() == "":
#     print("Пароль пустой! Введи пароль")
# else:
#     print("Неверный пароль")
#
# #2.1
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
#
# #2.2
# nums = [3, 4, 11, 4, 4]
# nums[2] = 100
# print(nums)
#
# #2.3
# my_list = []
#
# my_list.extend(range(1, 100, 3))
#
# print(my_list)
#
# my_list_new = list(range(1, 100, 3))
# print(my_list_new)

# #3.1
# menu_dish = {
#     "Борщ сибирский": 100,
#     "Пельмени с бараниной": 250,
#     "Селёдка под шубой": 200
# }
#
# menu_dish["Карпачо"] = 320
# print(menu_dish)
# menu_dish["Карпачо"] = 1100
# print(menu_dish)
#
# #3.2
# products = {"яблоко": 100, "банан": 50, "апельсин": 70}
# order = "яблоко" # или "черви"
#
# if order in products:
#     print(products[order])
# else:
#     print("У нас такого товара нет")

# #4.1
# for n in range(1, 6):
#     print(f"Квадрат числа {n} = {n ** 2}")
#
# #4.2
n = 10
total = 0
for n in range(1, n + 1): # n + 1 потому что в диапазоне не учитывается конечное значение
    total += n
print(total)
#
# # без цикла
# n = 10
# sum_n = sum(range(1, n + 1))
# print(sum_n)
#
# #4.3
# num = range(10, 0, -1)
#
# for n in num:
#     print(n)
#
# #4.4
# fruits = ["яблоко", "банан", "груша"]
#
# for fruit in fruits:
#     print(fruit)
#
# #4.5
# numbers = [3, 8, 1, 9, 4]
# max_num = numbers[0]
# for n in numbers:
#     if n > max_num:
#         max_num = n
# print(max_num)
#
# # без цикла
# new_num = max(numbers)
# print(new_num)
#
# #4.6
# products = {"яблоко": 100, "банан": 50, "апельсин": 70}
#
# sum_price = sum(products.values())
# print(sum_price)

#5.1
# n = 1
#
# while n <= 10:
#     print(n)
#     n += 1
# #5.2
# n = 10
# i = 1
# total = 0
#
# while i <= n:
#     total += i
#     i += 1
# print(total)
# # 5.3
# nums = [2, 7, 4, 9, 6, 5]  # исходный список
# i = 0  # начальный индекс
#
# while i < len(nums):  # цикл работает, пока индекс в пределах списка
#     if nums[i] % 2 == 0:  # если элемент чётный
#         del nums[i]  # удаляем его (список укорачивается, i не увеличиваем)
#     else:
#         i += 1  # если элемент нечётный — переходим к следующему
# print(nums)  # выводим обновлённый список без чётных чисел

#6.1
# a = [1, 2, 3]
#
# b = a
# b[0] = 100
# print(a, b)
#
# a = [1, 2, 3]
#
# b = a.copy()
# b[0] = 100
# print(a, b)

#7.1
# time = 6600
#
# h = time // 3600
# m = (time % 3600) // 60
# s = time % 60
#
# print(f"{h} час {m} минута {s} секунда")

