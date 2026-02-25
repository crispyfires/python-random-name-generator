import random

forenames_m_en = [
    "David",
    "John",
    "James",
    "George",
    "Harold",
    "Paul",
    "Peter",
    "Mark",
    "Alan",
    "Anthony",
    "William",
    "Thomas",
    "Timothy",
    "Brian",
    "Simon",
    "Ian",
    "Christopher",
    "Robert",
    "Steven",
    "Daniel",
    "Martin",
    "Matthew",
    "Graham",
    "Neil",
    "Keith",
    "Edward",
    "Nicholas",
]

forenames_f_en = [
    "Susan",
    "Margaret",
    "Sarah",
    "Sara",
    "Patricia",
    "Elizabeth",
    "Mary",
    "Helen",
    "Victoria",
    "Emma",
    "Olivia",
    "Linda",
    "Bertha",
    "Jane",
    "Janet",
    "Lisa",
    "Claire",
    "Barbara",
]

surnames_en = [
    "Smith",
    "Jones",
    "Taylor",
    "Fletcher",
    "Cooper",
    "Miller",
    "Johnson",
    "Davies",
    "Thompson",
    "Thomson",
    "Wood",
    "Harris",
]


def generate_name_m_en():
    forename_m_en = random.choice(forenames_m_en)
    middlename_m_en = random.choice(forenames_m_en)
    surname_m_en = random.choice(surnames_en)
    return forename_m_en + " " + middlename_m_en + " " + surname_m_en


def generate_name_f_en():
    forename_f_en = random.choice(forenames_f_en)
    middlename_f_en = random.choice(forenames_f_en)
    surname_f_en = random.choice(surnames_en)
    return forename_f_en + " " + middlename_f_en + " " + surname_f_en
