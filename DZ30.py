class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print(f"{self.name} => ", end="")
        self.laptop.show()

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.memory = 16

        def show(self):
            print(f"{self.model}, {self.cpu}, {self.memory}")


student1 = Student("Roman")
student1.show()

student2 = Student("Vladimir")
student2.show()
