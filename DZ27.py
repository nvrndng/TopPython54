# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
#         print("*" * 40)
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print(f"Информация о счете")
#         print("-" * 30)
#         print(f"# {self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 30)
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.percent * self.value
#         print(f"Проценты успешно выплачены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению, у вас нет {val} {Account.suffix}")
#
#         else:
#             self.value -= val
#             print(f" было успешно снято")
#             self.print_balance()
#
#
#     def plus_money(self, val):
#             self.value += val
#             print(f"Было успешно добавлено {val} {Account.suffix}!")
#             self.print_balance()
#
#     def __del__(self):
#         print(f"Счет #{self.num}, принадлежащий {self.surname} был успешно закрыт!")
#
#
# acc = Account("123456", "Долгих", 0.03, 1000)
# acc.print_info()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_eur_rate(3)
# acc.edit_owner("Дюма")
# acc.print_info()
#
# print()
# acc.add_percents()
#
# acc.withdraw_money(1000)
# acc.plus_money(5000)





# #a.через обычные сеттеры и геттеры
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт")
#         print("*" * 40)
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 30)
#         print(f"# {self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 30)
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"{usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"{eur_val} {Account.suffix_eur}")
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print("Недостаточно средств")
#         else:
#             self.__value -= val
#
#     def plus_money(self, val):
#         self.__value += val





#b. через @property

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value

    @property
    def num(self):
        return self.__num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value):
        self.__percent = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def print_info(self):
        print("Информация о счете")
        print(f"№: {self.__num}")
        print(f"Владелец: {self.__surname}")
        print(f"Баланс: {self.__value} RUB")
        print(f"Процент: {self.__percent:.0%}")

    def add_percents(self):
        self.__value += self.__value * self.__percent

    def withdraw_money(self, val):
        if val > self.__value:
            print("Недостаточно средств")
        else:
            self.__value -= val

    def plus_money(self, val):
        self.__value += val