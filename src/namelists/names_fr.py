import random

forenames_m_fr = [
    "Jacques",
    "Jean",
    "Michel",
    "Pierre",
    "Jean-Baptiste",
    "Jean-Luc",
    "Jean-Paul",
    "Claude",
    "Frédéric",
    "Philippe",
    "Alain",
    "Bernard",
    "André",
    "Thierry",
    "Christophe",
    "Laurent",
    "Pascal",
    "René",
    "Olivier",
    "Emmanuel",
    "Nicolas",
    "Sébastien",
    "Charles",
    "Georges",
    "François",
    "Valéry",
    "Henri",
    "Louis",
]

forenames_f_fr = [
    "Marie",
    "Jeanne",
    "Marguerite",
    "Élisabeth",
    "Jacqueline",
    "Anne-Sophie",
    "Nathalie",
    "Isabelle",
    "Catherine",
    "Véronique",
    "Suzanne",
    "Henriette",
    "Madeleine",
    "Bernadette",
    "Gisèle",
    "Yvonne",
    "Claudine",
    "Sylviane",
    "Hélène",
    "Violette",
    "Cécile",
    "Charlotte",
    "Joséphine",
    "Dominique",
    "Éveline",
    "Amélie",
    "Paulette",
]

surnames_fr = [
    "Delacroix",
    "Dubois",
    "Martin",
    "Bernard",
    "Petit",
    "Durand",
    "Leroy",
    "Thomas",
    "Lambert",
    "Leclercq",
    "Laurent",
    "Lejeune",
    "Dumont",
    "Dupont",
    "Simon",
    "Tremblay",
    "Gagnon",
    "Bouchard",
    "Gauthier",
    "Gagné",
    "Lavoie",
    "Fortin",
    "Morin",
]


def generate_name_m_fr():
    forename_m_fr = random.choice(forenames_m_fr)
    surname_f_en = random.choice(surnames_fr)
    return forename_m_fr + " " + surname_f_en


def generate_name_f_fr():
    forename_f_fr = random.choice(forenames_f_fr)
    surname_f_fr = random.choice(surnames_fr)
    return forename_f_fr + " " + surname_f_fr
