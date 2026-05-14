class ValueCheck:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.name in ["_price", "_count"]:
            if value <= 0:
                raise ValueError("Число должно быть положительным!")

        setattr(instance, self.name, value)

class Order:
    price = ValueCheck()
    count = ValueCheck()

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def allOrder(self):
        return self.price * self.count

    def __str__(self):
        return f"Order('{self.name}', {self.price}, {self.count})"

ord1 = Order("apple", 5, 10)

print(ord1)
print(ord1.allOrder())

# ord2 = Order("banana", -4, 2)
# print(ord2)

ord3 = Order("orange", 34, 24)
print(ord3)
print(ord3.allOrder())