import pickle

def load_file():
    try:
        with open("land.txt", "rb") as f:
            file = pickle.load(f)
    except FileNotFoundError:
        file = {}

    return file

def save_file(file):
    with open("land.txt", "wb") as f:
        pickle.dump(file, f)
    print("Файл сохранен")

def check_val(text):
    return text.isalpha() and text.istitle()

while True:
    print("*" * 40)
    print("Выбор действия:")
    print("1 - добавление данных")
    print("2 - удаление данных")
    print("3 - поиск данных")
    print("4 - редактирование данных")
    print("5 - просмотр данных")
    print("6 - завершение работы")

    choice = input("Ввод: ")

    if not choice.isdigit():
        print("Необходимо ввести цифру!")
        continue

    file = load_file()

    if choice == "1":
        land = input("Введите название страны (с заглавной буквы): ")
        city = input("Введите название столицы (с заглавной буквы): ")

        if not check_val(land):
            print("Название страны должно быть написано с заглавной буквы!")
            continue

        if not check_val(city):
            print("Название города должно быть написано с заглавной буквы!")
            continue

        file[land] = city
        save_file(file)


    elif choice == "2":
        land = input("Введите название страны, чтобы удалить: ")

        if not check_val(land):
            print("Название страны должно быть написано с заглавной буквы!")
            continue

        if land in file:
            del file[land]
            save_file(file)
            print("Данные удалены!")
        else:
            print("Такая страна не найдена!")


    elif choice == "3":
        land = input("Введите название страны для поиска: ")

        if not check_val(land):
            print("Название страны должно быть написано с заглавной буквы!")
            continue

        if land in file:
            print(land, "-", file[land])
        else:
            print("Такая страна не найдена!")


    elif choice == "4":
        land = input("Введите название страны: ")

        if not check_val(land):
            print("Название страны должно быть написано с заглавной буквы!")
            continue

        if land in file:
            new_land = input("Введите новый город: ")

            if not check_val(new_land):
                print("Название города должно быть написано с заглавной буквы!")
                continue

            file[land] = new_land
            save_file(file)
            print("Данные изменены!")
        else:
            print("Такая страна не найдена!")


    elif choice == "5":
        if len(file) == 0:
            print("Файл пуст!")
        else:
            for land, city in file.items():
                print(land, "-", city)


    elif choice == "6":
        print("Завершение работы")
        break


    else:
        print("Некорректный ввод!")