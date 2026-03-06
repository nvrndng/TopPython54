import math

def figures_area(figure_type, **kwargs):

    if figure_type == "rombus":
        d1 = kwargs.get('d1')
        d2 = kwargs.get('d2')
        if d1 and d2:
            return (d1 * d2) / 2
        return()

    elif figure_type == "square":
        a = kwargs.get('a')
        if a:
            return a ** 2
        return()

    elif figure_type == "trapezoid":
        a = kwargs.get('a')
        b = kwargs.get('b')
        h = kwargs.get('h')
        if a and b and h:
            return 0.5 * (a + b) * h
        return()

    elif figure_type == "circle":
        r = kwargs.get('r')
        if r:
            return math.pi * r ** 2
        return()

    else:
        if figure_type == "unknow":
            a = kwargs.get('a')
            b = kwargs.get('b')
            c = kwargs.get('c')
            if a and b and c:
                return "invalid data"
        return()


print(figures_area("rombus", d1=10, d2=8))
print(figures_area("square", a=5))
print(figures_area("trapezoid", a=12, b=3, h=6))
print(figures_area("circle", r=18))
print(figures_area("unknow", a=1, b=2, c=3))

