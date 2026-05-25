# #№1
#
# class CheckValue:
#     @classmethod
#     def check_value(cls, value):
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError("Сторона должна быть целым положительным числом!")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.check_value(value)
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = CheckValue()
#     b = CheckValue()
#     c = CheckValue()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def IsTriangleOk(self):
#         if (
#             self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
#         ):
#             return True
#         return False
#
#     def __str__(self):
#         if self.IsTriangleOk():
#             return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует."
#         else:
#             return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует."
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
#
# print(t1)
# print(t2)
# print(t3)


#2


from geomerty.circle import Circle
from geomerty.rectangle import Rectangle
from geomerty.cylinder import Cylinder

circles = [Circle(2), Circle(4), Circle(7), Circle(5), Circle(9), Circle(1), Circle(3), Circle(13), Circle(8)]
rect = [Rectangle(2, 3), Rectangle(4, 8), Rectangle(9, 9), Rectangle(7, 3)]
cylinders = [Cylinder(2, 3), Cylinder(5, 6), Cylinder(7, 8)]

cirle_max_s = max(circles, key=lambda c: c.get_circle_area())
rect_min_p = min(rect, key=lambda r: r.get_rect_perimetr())
cylinders_v = list(map(lambda c: c.get_v(), cylinders))
cylinders_v_avr = sum(cylinders_v) / len(cylinders_v)


print("*" * 20)
print(f'Окружность с наибольшей площадью: {cirle_max_s.print_circle()} = {cirle_max_s.get_circle_area()}')
print(f'Прямоугольник с наименьшим периметром {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimetr()}')
print(f'Средний объем цилиндров {round(cylinders_v_avr, 2)}')