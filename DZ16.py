#1

def repeat(n):
    def decor(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decor

@repeat(3)
def say_hello():
    print("Hello")

say_hello()


#2

def my_decorator(func):
    def wrapper(a, b):
        my_res = func(a, b)
        return my_res * 2
    return wrapper

@my_decorator
def res_double(a, b):
    return a + b

print(res_double(2,3))


#3

is_admin = False
#is_admin = True

def am_i_admin(func):
    def wrapper():
        if is_admin:
            print("Hello World")
        else:
            print("Доступ запрещен!")
    return wrapper

@am_i_admin
def say_hello():
    pass

say_hello()


#4

def intro_outro(func):
    def wrapper():
        print("Начало")
        func()
        print("Конец")
    return wrapper

@intro_outro
def say_hello():
    print("Привет!")

say_hello()