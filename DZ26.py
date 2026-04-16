# #1
#
# import math #импортирую математический модуль
#
# class Rectangle: #создаю класс прямоугольник
#
#     def __init__(self, width=0, height=0): #создаю инструктор, задам значения (динамические св-ва) по умолчанию на 0
#         self.__width = width #приватный метод, ширина прямоугольника
#         self.__height = height #приватный метод, высота прямоугольника
#
#     def set_width(self, width): #сеттер ширины, задаем параметры
#         self.__width = width
#
#     def get_width(self): #геттер, возвращает ширину
#         return self.__width
#
#     def set_height(self, height): #сеттер высоты, задаем параметры
#         self.__height = height
#
#     def get_height(self): #геттер, возвращает высоту
#         return self.__height
#
#     def area(self): #метод, считающий площадь
#         return self.get_width() * self.get_height()
#
#     def perimeter(self): #метод, считающий периметр
#         return 2 * (self.get_width() + self.get_height())
#
#     def gipotenuza(self): #метод, высчитывающий гипотенузу
#         return math.sqrt(self.get_width() ** 2 + self.get_height() ** 2)
#
#     def paint_rec(self): #рисуем прямоугольник звездочками
#         for i in range(self.get_height()):
#             print("*" * self.get_width())
#
#
# r = Rectangle() #создаю экземпляр. далее обращаюсь к методам через этот экземпляр
# r.set_width(9) #задаю ширину
# r.set_height(3) #задаю высоту
# print("Высота прямоугольника: ", r.get_height())
# print("Ширина прямоугольника: ", r.get_width())
# print("Площадь прямоугольника: ", r.area())
# print("Периметр прямоугольника: ", r.perimeter())
# print("Гипотенуза прямоугольника: ", r.gipotenuza())
#
# r.paint_rec()



#2


class Konverter: #создаю класс конвертер
    def __init__(self, kg=0): #создаю инструктор с кг
        self.__kg = kg #приватное свойство

    @property #указываю декоратор проперти
    def kg(self): #геттер
        return self.__kg

    @kg.setter #сеттер
    def kg(self, value):
        if isinstance(value, (int, float)): #проверка типа, если заданный параметр число, целое или плавающее
            self.__kg = value #устанавливает значение при прохождении проверки
        else:
            print("Нужно ввести число!")

    def kg_to_pounds(self): #метод, который будет конвертировать
        return self.__kg * 2.205 #возвращает переведенные в фунты кг


k1 = Konverter()
k1.kg = 12 #тут обращаюсь к декоратору и задаю св-во
print(f"{k1.kg} кг => {round(k1.kg_to_pounds(), 2)} фунтов") #округляю результат до двух симв. после зпт
