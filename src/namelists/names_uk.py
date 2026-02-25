import random

forenames_m_uk = [
    "Dmytro",
    "Vladyslav",
    "Volodymyr",
    "Anatolii",
    "Kostiantyn",
    "Sviatoslav",
    "Petro",
    "Ivan",
    "Yevhen",
    "Danylo",
    "Ihor",
    "Mykhailo",
    "Viacheslav",
    "Maksym",
    "Vasyl",
    "Pavlo",
    "Viktor",
    "Borys",
    "Mykola",
    "Bohdan",
    "Oleksander",
    "Kyrylo",
    "Vitalii",
    "Oleksandr",
    "Artem",
]

forenames_f_uk = [
    "Iryna",
    "Halyna",
    "Kateryna",
    "Oksana",
    "Khrystyna",
    "Olha",
    "Oleksandra",
    "Mariia",
    "Sofiia",
    "Tatiana",
    "Svitlana",
    "Olena",
    "Liudmyla",
    "Hanna",
    "Larysa",
]

patronymics_m_uk = ["Ivanovych", "Dmytrovych", "Vasylovych", "Serhiiovych"]

patronymics_f_uk = ["Ivanivna", "Dmytrivna", "Vasylivna", "Serhiivna"]

surnames_m_uk = [
    "Voloshyn",
    "Zelenskyi",
]
surnames_f_uk = ["Voloshyna", "Zelenska"]
surnames_n_uk = [
    "Kovalchuk",
    "Koval",
    "Bondar",
    "Bondarchuk",
    "Tkachenko",
    "Shevchenko",
    "Kovalenko",
    "Nimchuk",
    "Dziuba",
    "Adamchuk",
    "Antonenko",
    "Dmytrenko",
]

surnames_mn_uk = surnames_m_uk + surnames_n_uk
surnames_fn_uk = surnames_f_uk + surnames_n_uk


def generate_name_m_uk():
    forename_m_uk = random.choice(forenames_m_uk)
    patronymic_m_uk = random.choice(patronymics_m_uk)
    surname_m_uk = random.choice(surnames_mn_uk)
    return forename_m_uk + " " + patronymic_m_uk + " " + surname_m_uk


def generate_name_f_uk():
    forename_f_uk = random.choice(forenames_f_uk)
    patronymic_f_uk = random.choice(patronymics_f_uk)
    surname_f_uk = random.choice(surnames_fn_uk)
    return forename_f_uk + " " + patronymic_f_uk + " " + surname_f_uk
