from faker import Faker
import random
import string
from data.data import Person, Color

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def get_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(1, 100),
        department=faker_ru.job(),
        salary=random.randint(100, 1000000),
        mobile=faker_ru.msisdn()
    )


def generated_file_txt():
    path = rf"C:\Users\svlip\PycharmProjects\demoqa\test{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:
        f.write(f"""Hello World{random.randint(0, 999)}""")
        f.close()
    return f.name, path


def random_num():
    return random.randint(1, 10)


def random_letter():
    return chr(random.randint(ord('a'), ord('z')))


def generator_color():
    yield Color(
        color_name=["Red", "Blue", "Yellow", "Purple", "White", "Violet",
                    "Indigo", "Black", "Magenta", "Aqua", "Green"]
    )
