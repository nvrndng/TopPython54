from geomerty.circle import Circle
from geomerty.rectangle import Rectangle

class Cylinder(Rectangle, Circle):
    def __init__(self, r, h):
        Circle.__init__(self, r)
        Rectangle.__init__(self, self.get_circle_circumference(), h)

    def get_v(self):
        res = self.get_circle_area() * self.h
        print(f"Объем цилиндра {round(res, 2)}")
        return res

    def print_cylinder(self):
        print(f"Радиус основания {self.r}, высота {self.h}")


