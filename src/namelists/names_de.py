import random

forenames_m_de = [
    "Johann",
    "Hans",
    "Martin",
    "Jakob",
    "Lukas",
    "Tobias",
    "Jan",
    "Thorsten",
    "Dirk",
    "Jürgen",
    "Erhard",
    "Jens",
    "Heiko",
    "Bernhard",
    "Carsten",
    "Fabian",
    "Fritz",
]
forenames_f_de = ["Anna", "Sabine", "Katrin"]
surnames_de = [
    "Müller",
    "Schmidt",
    "Schneider",
    "Fischer",
    "Weber",
    "Meyer",
    "Wagner",
    "Becker",
    "Schulz",
    "Hoffmann",
    "Schäfer",
    "Koch",
    "Bauer",
    "Richter",
    "Klein",
    "Wolf",
    "Schröder",
    "Neumann",
    "Schwarz",
    "Zimmermann",
    "Braun",
    "Krüger",
    "Hofmann",
    "Hartmann",
    "Lange",
    "Schmitt",
    "Werner",
    "Schmitz",
    "Krause",
    "Meier",
    "Lehmann",
    "Schmid",
    "Schulze",
    "Maier",
    "Köhler",
    "Herrmann",
    "König",
    "Walter",
    "Mayer",
    "Huber",
    "Kaiser",
    "Fuchs",
    "Peters",
    "Lang",
    "Scholz",
]


def generate_name_m_de():
    forename_m_de = random.choice(forenames_m_de)
    middlename_m_de = random.choice(forenames_m_de)
    surname_de = random.choice(surnames_de)
    return forename_m_de + " " + middlename_m_de + " " + surname_de


def generate_name_f_de():
    forename_f_de = random.choice(forenames_f_de)
    middlename_f_de = random.choice(forenames_f_de)
    surname_de = random.choice(surnames_de)
    return forename_f_de + " " + middlename_f_de + " " + surname_de
