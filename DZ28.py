class Point(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x},{self.__y})"

    def get_coords(self):
        return self.__x,self.__y

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "green", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        self._sp = sp
        self._ep = ep

class Line(Prop):

    def draw_line(self):
        x1, y1 = self._sp.get_coords()
        x2, y2 = self._ep.get_coords()

        if not isinstance(x1, int) or not isinstance(y1, int) or not isinstance(x2, int) or not isinstance(y2, int):
            print("Координаты должны быть целочисленными!")
            return

        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):

    def draw_rect(self):
        x1, y1 = self._sp.get_coords()
        x2, y2 = self._ep.get_coords()

        if not isinstance(x1, (int, float)) or not isinstance(y1, (int, float)) or not isinstance(x2, (int, float)) or not isinstance(y2, (int, float)):
            print("Координаты должны быть числом!")
            return

        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


l1 = Line(Point(1, 2), Point(10, 20), "red", 1)
l1.draw_line()

l2 = Line(Point(10.2, 20), Point(100, 200), "green", 3)
l2.draw_line()

r1 = Rect(Point(7, 9), Point(12, 15), "red", 3)
r1.draw_rect()

r2= Rect(Point(30.5, 40.2), Point(50, 60), "red", 1)
r2.draw_rect()