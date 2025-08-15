"""Задание 1."""
# class UserAccount:
#     def __init__(self, username: str, balance: float, password: str):
#         self.username = username
#         self._balance = balance
#         self.__password = password
#         self.__logged_in = False
#
#     def deposit(self, amount: float):
#         if amount > 0:
#             self._balance += amount
#             print(f"На счёт добавлено {amount}. Новый баланс: {self._balance}")
#         else:
#             print("Сумма должна быть положительной.")
#
#     def withdraw(self, amount: float):
#         if amount <= 0:
#             print("Сумма должна быть положительной.")
#         elif amount > self._balance:
#             print("Ошибка: недостаточно средств.")
#         else:
#             self._balance -= amount
#             print(f"Снято {amount}. Новый баланс: {self._balance}")
#
#     def login(self, password: str):
#         if password == self.__password:
#             self.__logged_in = True
#             print("Доступ разрешён")
#         else:
#             self.__logged_in = False
#             print("Доступ запрещён")
#
#     def get_balance(self):
#         if self.__logged_in:
#             return self._balance
#         else:
#             print("Ошибка: пользователь не авторизован.")
#
#
# acc = UserAccount("Ivan", 1000, "qwerty")
#
# acc.deposit(500)
# acc.withdraw(200)
# acc.get_balance()
#
# acc.login("wrong")
# acc.login("qwerty")
# print(acc.get_balance())

"""Задание 2."""

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self) -> str:
        pass

    @abstractmethod
    def fuel_type(self) -> str:
        pass

class Car(Transport):
    def move(self) -> str:
        return "Машина едет по дороге"

    def fuel_type(self) -> str:
        return "Бензин"


class Bike(Transport):
    def move(self) -> str:
        return "Велосипед едет по дороге"

    def fuel_type(self) -> str:
        return "Сила  велосипедиста"

class Plane(Transport):
    def move(self) -> str:
        return "Самолёт летит в небе"

    def fuel_type(self) -> str:
        return "Керосин"


vehicles = [Plane(), Car(), Bike()]

for v in vehicles:
    print(v.move())
    print("Топливо:", v.fuel_type())
    print()