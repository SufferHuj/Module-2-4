# # 1 задание создание приложения для интернет-магазина
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name} : {self.price} руб."
#
# class Catalog:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def show_products(self):
#         for product in self.products:
#             print(product)
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_to_cart (self, product, quantity):
#         if quantity < 0:
#             print("Количество должно быть положительным")
#             return
#
#         self.items.append({"product": product, "quantity": quantity})
#
#     def calculate_price(self):
#         return sum(item["product"].price * item["quantity"] for item in self.items)
#
#     def show_cart(self):
#         for item in self.items:
#             product = item["product"]
#             quantity = item["quantity"]
#             print(f"{product.name} * {quantity} = {product.price * quantity} руб.")
#
# class Order:
#     def __init__(self, cart):
#         self.cart = cart
#         self.status = "Pending"
#
#     def complete_order(self):
#         total_price = self.cart.calculate_price()
#         self.status = "Completed"
#         return f"Заказ завершён! Итоговая сумма {total_price} руб."
#
#
# product_1 = Product("Ноутбук", 20000)
# product_2 = Product("Мышь проводная", 500)

# catalog = Catalog()
# catalog.add_product(product_1)
# catalog.add_product(product_2)
# catalog.show_products()

# cart_1 = Cart()
# cart_1.add_to_cart(product_1, 1)
# cart_1.add_to_cart(product_2, 2)
# cart_1.show_cart()
#
# order = Order(cart_1)
# print(order.complete_order())

# 1 задание функции
# def restore_health(current_health, potion):
#     max_health = 100
#     new_health = current_health + potion
#
#     if new_health > max_health:
#         return max_health
#     else:
#         return new_health
#
# unit_1 = restore_health(90, 15)
# unit_2 = restore_health(50, 30)
#
# print("ХП первого перса =", unit_1)
# print("ХП второго перса =", unit_2)

# 2 задание методы класса
# class GoblinTrader:
#     def __init__(self, gold):
#         self.gold = gold
#
#     def buy_item(self, item_name, item_price):
#
#         if self.gold >= item_price:
#             self.gold -= item_price
#             print("Куплен:", item_name, "У тебя осталось:", self.gold, "золота!")
#
#         else:
#             print("Недостаточно золота!")
#
# goblin_1 = GoblinTrader(200)
# goblin_1.buy_item("Свиток скорости", 199)

# задача 2.1 методы класса и статические методы

# class GoblinMarket:
#     def __init__(self, gold):
#         self.gold = gold
#
#     @staticmethod
#     def tax_rate():
#         return 0.1
#
#     @classmethod
#     def from_rich_merchant(cls):
#         return cls(1000)
#
#     def buy_item(self, item_name, item_price):
#
#         total_price = item_price + item_price * self.tax_rate()
#
#         if self.gold >= total_price:
#
#             self.gold -= total_price
#
#             print("Успешная покупка! У тебя осталось", int(self.gold), "золота")
#
#         else:
#             print("Недостаточно золота!")
#
# goblin_1 = GoblinMarket(150)
# goblin_1.buy_item("Амулет удачи", 150)
#
# goblin_2 = GoblinMarket.from_rich_merchant()
# goblin_2.buy_item("Волшебный посох", 500)

# # 3 задание наследование
# class Hero:
#
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def take_damage(self, damage):
#         self.health -= damage
#         print(f"{self.name} получил {damage} урона. У него осталось {self.health} здоровья")
#
# class Warrior(Hero):
#
#     def attack(self):
#         return "Нанёс 20 урона мечом"
#
# class Mage(Hero):
#
#     def attack(self):
#         return "Нанёс 15 урона заклинанием"
#
# warrior = Warrior("Conan", 120)
# mage = Mage("Zina", 80)
#
# print(warrior.attack())
# print(mage.attack())
#
# warrior.take_damage(30)
# mage.take_damage(20)

# задание 4 полиморфизм
# class Peon:
#     def work(self):
#         return "Собирает золото"
#
# class Knight:
#     def work(self):
#         return "Сражается с врагами"
#
# def daily_work(hero):
#     return hero.work()
#
# peon = Peon()
# knight = Knight()
#
# print(daily_work(peon))
# print(daily_work(knight))

# # задание 5 абстракция
# from abc import ABC, abstractmethod
#
# class Artifact(ABC):
#
#     @abstractmethod
#     def activate(self):
#         pass
#
# class HealthArtifact(Artifact):
#     def activate(self):
#         return "Восстановлено 50 здоровья"
#
# class DamageArtifact(Artifact):
#     def activate(self):
#         return "Нанесено 30 урона врагу"
#
# heal_artifact = HealthArtifact()
# damage_artifact = DamageArtifact()
#
# print(heal_artifact.activate())
# print(damage_artifact.activate())

# задание 6 инкапсуляция
# class GoblinBank:
#
#     def __init__(self, gold):
#
#         if gold < 0:
#             raise ValueError("Золото не может быть отрицательным!")
#
#         self.__gold = gold
#
#     def get_gold(self):
#         return self.__gold
#
#     def deposit_gold(self, amount):
#
#         if amount > 0:
#             self.__gold += amount
#             return f"Добавлено {amount} золота. Текущий баланс: {self.__gold}"
#         else:
#             return "Не обманывай меня! Золото не может иметь отрицательное значение"
#
#     def withdraw_gold(self, amount):
#
#         if amount > self.__gold:
#             return "В твоём кошельке недостаточно золота!"
#
#         elif amount > 0:
#             self.__gold -= amount
#             return f"Снято {amount} золота. Текущий баланс: {self.__gold}"
#
#         else:
#             return "Золота должна быть больше 0!"
#
# g_bank = GoblinBank(100)
#
# print(g_bank.deposit_gold(55))
# print(g_bank.withdraw_gold(156))
#
# print("У тебя осталось:", g_bank.get_gold(), "золота")

# задание 7 декораторы
# def health_boost(func):
#
#     def wrapper(current_health, health_restore, hero_level):
#
#         if hero_level > 10:
#              health_restore *= 2
#         return func(current_health, health_restore)
#
#     return wrapper
#
# @health_boost
# def drink_from_well(current_health, health_restore):
#
#     max_health = current_health + health_restore
#
#     if max_health > 100:
#         max_health = 100
#
#     return max_health
#
# hero_1 = drink_from_well(80, 11, 11)
#
# print("Здоровье твоего героя:", hero_1)