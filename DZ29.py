class Liquid:
    def __init__(self, name, plotnost):
        self._plotnost = plotnost
        self._name = name
        if not isinstance(name, str):
            print("Название должно быть строкой!")
            return
        if not isinstance(plotnost, (int, float)):
            print("Плотность должна быть числом!")
            return




    def new_plotnost(self, plotnost):
        if not isinstance(plotnost, (int, float)):
            print("Плотность должна быть числом!")
            return

    def plus_mass(self, v):
        if not isinstance(v, (int, float)):
            print("Масса должна быть числом!")
            return

        return self._plotnost * v

    def plus_v(self, mass):
        if not isinstance(mass, (int, float)):
            print("Объем должен быть числом!")
            return

        return mass / self._plotnost

    def print_info(self):
        print(f"Жидкость '{self._name}' (плотность = {self._plotnost} kg/m3)")

class Alcohol(Liquid):
    def __init__(self, name, plotnost, krep):
        super().__init__(name, plotnost)
        self._krep = krep

        if not isinstance(krep, (int, float)):
            print("Крепость должна быть числом!")
            return

    def new_krep(self, krep):

        if not isinstance(krep, (int, float)):
            print("Крепость должна быть числом!")
            return

        self._krep = krep

    def print_krep(self):
        print(self._krep)

a = Alcohol("Wine", 1064.2, 14)
a.print_info()

a.new_krep(20)
a.print_krep()

print()

m = a.plus_mass(0.5)
print(f"Вес 0.5 m3 Wine составляет {m} кг")

v = a.plus_v(300)
print(f"Объем 300 кг Wine равен {v} m3")

print()

a.print_krep()

a.new_krep(20)
a.print_krep()