#1

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict4 = dict1 | dict2 | dict3
print(dict4)


#2

people = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

for key in people:
    print(key)
    print('name', people[key]['name'])
    print('salary', people[key]['salary'])
    print()

while True:
    n = input("Введите номер сотрудника(emp1, emp2, emp3): ")
    if n == "0":
        break
    if n in people:
        try:
            sal = int(input("Укажите новую зарплату: "))
            people[n]['salary'] = sal
            for key in people:
                print(key)
                print('name', people[key]['name'])
                print('salary', people[key]['salary'])
                print()
        except ValueError:
            print("Зарплату надо ввести числом!")
    else:
        print("Нет такого сотрудника")

# for key in people:
#     print(key)
#     print('name', people[key]['name'])
#     print('salary', people[key]['salary'])
#     print()