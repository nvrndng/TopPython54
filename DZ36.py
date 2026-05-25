import pickle
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    # print(name)

    while len(tel) != 10:
        tel += choice(nums)

    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_pickle(person_dict, num):
    try:
        with open('persons.pickle', 'rb') as f:
            data = pickle.load(f)

    except FileNotFoundError:
        # data = []
        data = {}

    data[num] = person_dict

    with open('persons.pickle', 'wb') as f:
        pickle.dump(data, f)


for i in range(5):
    person, tel = gen_person()
    write_pickle(person, tel)

with open('persons.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)
