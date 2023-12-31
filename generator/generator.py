from faker import Faker
import random
import string
from data.data import Person, Color, Date, FormsData

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


def get_time():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 3) * 15
    time_str = f'{hours:02d}:{minutes:02d}'
    return time_str


def generator_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time=get_time()
    )


def random_num_up_to_one_hundred():
    x = random.randint(0, 100)
    return x


def generated_subject():
    subject = FormsData.SUBJECT
    random.shuffle(subject)
    new_list = []
    for i in range(random.randint(1, 4)):
        new_list.append(subject[i])
    return new_list


def generated_file():
    path = rf"C:\Users\svlip\PycharmProjects\demoqa\test{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:
        f.write(f"""Hello World{random.randint(0, 999)}""")
        f.close()
    return f.name, path


def generated_city():
    random_list = random.choice(["NCR", "Haryana", "Rajasthan"])
    city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer", ]
    }
    return random_list, city[random_list]
