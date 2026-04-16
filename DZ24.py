import os
from datetime import datetime

p = input("Укажите путь: ")

if not os.path.exists(p):
    print("Такого пути или файла не существует!")
else:
    abs_p = os.path.abspath(p)
    print("Путь: ", abs_p)

    if os.path.isfile(p):
        print("Тип - Файл")
        size = os.path.getsize(p)
        print("Размер файла ", size, "байт")

        time = os.path.getmtime(p)
        last_time = datetime.fromtimestamp(time).strftime('%d.%m.%Y %H:%M:%S')
        print("Последнее изменение файла: ", last_time)

    elif os.path.isdir(p):
        print("Тип - Директория ")