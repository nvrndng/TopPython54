class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        if not isinstance(x, (int, float)):
            raise TypeError("X должен быть числом!")

        if not isinstance(y, (int, float)):
            raise TypeError("Y должен быть числом!")

        if not isinstance(z, (int, float)):
            raise TypeError("Z должен быть числом!")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __getitem__(self, item):
        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        elif item == "z":
            return self.z

    def __setitem__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом!")

        if key == "x":
            self.x = value
        elif key == "y":
            self.y = value
        elif key == "z":
            self.z = value

p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)

print("Координаты 1-й точки: ", p1.x, p1.y, p1.z)
print("Координаты 2-й точки: ", p2.x, p2.y, p2.z)

print("Сложение координат: ", p1 + p2)
print("Вычитание координат: ", p1 - p2)
print("Умножение: ", p1 * p2)
print("Деление: ", p1 / p2)

print("Равенство координат: ", p1 == p2)

print("x =", p1["x"], "x1 =", p2["x"])
print("y =", p1["y"], "y1 =", p2["y"])
print("z =", p1["z"], "z1 =", p2["z"])

p1["x"] = 20
print("Запись значения в координату x: ", p1["x"])