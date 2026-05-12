from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def fullinfo(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        super().__init__(color)
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2

    def draw(self):
        for i in range(self.a):
            print("*" * self.a)

    def fullinfo(self):
        print("===Квадрат===")
        print(f"Сторона: {self.a}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Rectangle(Shape):
    def __init__(self, width, length, color):
        super().__init__(color)
        self.width = width
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length

    def draw(self):
        for i in range(self.width):
            print("*" * self.length)

    def fullinfo(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        a = self.perimeter() / 2
        return round(math.sqrt(a * (a - self.a) * (a - self.b) * (a - self.c)), 2)

    def draw(self):
        for i in range(1, self.a + 1, 2):
            print("*" * i)

    def fullinfo(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.a}")
        print(f"Сторона 2: {self.b}")
        print(f"Сторона 3: {self.c}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()

s1 = Square(3, "red")
s1.fullinfo()
print()
r1 = Rectangle(3, 7, "green")
r1.fullinfo()
print()
t1 = Triangle(11, 6, 6, "yellow")
t1.fullinfo()
print()

