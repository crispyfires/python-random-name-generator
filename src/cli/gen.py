import random

import click

import src.namelists.names_de
import src.namelists.names_en
import src.namelists.names_pl
import src.namelists.names_ru
import src.namelists.names_uk


@click.command()
@click.option(
    "--language",
    help="Specifies which language (in 2-digit ISO 639 codes) the name should come from. Use 'random' for random selection. Default is 'random'",
    default="random",
)
@click.option(
    "--number",
    help="Specifies amount of names outputted (in numerals). Default is '1'",
    type=int,
    default="1",
)
@click.option(
    "--gender",
    help="Specifies the gender of the name (m for male, f for female)",
    type=click.Choice(["m", "f"], case_sensitive=False),
    required=True,
)
def generate_name(language, gender, number):
    if language.lower() == "random":
        language = random.choice(["de", "en", "pl", "uk"])

    names = []
    for _ in range(number):
        if language.lower() == "uk":
            if gender.lower() == "m":
                name = src.namelists.names_uk.generate_name_m_uk()
            elif gender.lower() == "f":
                name = src.namelists.names_uk.generate_name_f_uk()
        elif language.lower() == "de":
            if gender.lower() == "m":
                name = src.namelists.names_de.generate_name_m_de()
            elif gender.lower() == "f":
                name = src.namelists.names_de.generate_name_f_de()
        elif language.lower() == "en":
            if gender.lower() == "m":
                name = src.namelists.names_en.generate_name_m_en()
            elif gender.lower() == "f":
                name = src.namelists.names_en.generate_name_f_en()
        elif language.lower() == "pl":
            if gender.lower() == "m":
                name = src.namelists.names_pl.generate_name_m_pl()
            elif gender.lower() == "f":
                name = src.namelists.names_pl.generate_name_f_pl()
        elif language.lower() == "ru":
            if gender.lower() == "m":
                name = src.namelists.names_ru.generate_name_m_ru()
            elif gender.lower() == "f":
                name = src.namelists.names_ru.generate_name_f_ru()
        else:
            click.echo("Language code not supported.")
            return

        names.append(name)

    for name in names:
        click.echo(name)


if __name__ == "__main__":
    generate_name()
