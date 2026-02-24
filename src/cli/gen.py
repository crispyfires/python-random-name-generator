import random

from typer import Option, Typer

from src.namelists import names_uk

app = Typer()


@app.command(
    "--language",
    help="Specifies which language (in 2-digit ISO 639 codes) the name should come from",
)
def language():
    if language == "uk":
        name = random.choice(names_uk.generate_name_m_uk())
        return print(f"{name}")


def gender():
    if gender == "m" and language == "uk":
        name = random.choice(names_uk.generate_name_m_uk())
        return print(f"{name}")
    if gender == "f" and language == "uk":
        name = random.choice(names_uk.generate_name_f_uk())
        return print(f"{name}")


if __name__ == "__main__":
    app()
