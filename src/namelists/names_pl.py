import random

fornames_m_pl = [
    "Radosław",
    "Czesław",
    "Grzegorz",
    "Sebastian",
    "Jan",
    "Janusz",
    "Amadeusz",
    "Piotr",
    "Paweł",
    "Arkadiusz",
    "Bogdan",
    "Szczepan",
    "Tomasz",
    "Maciej",
    "Jarosław",
    "Jerzy",
    "Konstanty",
    "Krzysztof",
    "Ksawery",
    "Leszek",
    "Łukasz",
    "Maksymilian",
    "Marcin",
    "Marek",
    "Mariusz",
    "Mateusz",
    "Michał",
    "Mieczysław",
    "Patryk",
    "Henryk",
    "Eryk",
    "Rafał",
    "Sławomir",
    "Mirosław",
    "Tadeusz",
    "Wiktor",
    "Władysław",
    "Włodzimierz",
    "Wojciech",
    "Zbigniew",
    "Karol",
    "Ignacy",
    "Andrzej",
    "Zygmunt",
    "Stanisław",
    "Jakub",
    "Artur",
    "Jacek",
    "Przemysław",
    "Bartosz",
    "Kazimierz",
]

surnames_m_pl = [
    "Bratkowski",
    "Kowalski",
    "Baliński",
    "Buczkowski",
    "Burzyński",
    "Drągowski",
    "Lewandowski",
    "Kamiński",
    "Zieliński",
    "Szymański",
    "Kozłowski",
    "Jankowski",
    "Wojciechowski",
    "Kwiatkowski",
    "Piotrowski",
    "Grabowski",
    "Majewski",
    "Jabłoński",
    "Olszewski",
]

surnames_n_pl = [
    "Dziura",
    "Dutkiewicz",
    "Adamiak",
    "Pietras",
    "Buczek",
    "Grzegorczyk",
    "Szczygieł",
    "Pietrzyk",
    "Cichoń",
    "Rybak",
]

surnames_mn_pl = surnames_m_pl + surnames_n_pl


def generate_name_m_pl():
    forname_m_pl = random.choice(fornames_m_pl)
    middlename_m_pl = random.choice(fornames_m_pl)
    surname_m_pl = random.choice(surnames_mn_pl)
    return forname_m_pl + " " + middlename_m_pl + " " + surname_m_pl
