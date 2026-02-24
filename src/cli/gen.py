import random

import click

import src.namelists.names_pl
import src.namelists.names_uk


@click.command()
@click.option(
    "--language",
    help="Specifies which language (in 2-digit ISO 639 codes) the name should come from. Use 'random' for random selection. Default is 'random'",
    default="random",
)
@click.option(
    "--gender",
    help="Specifies the gender of the name (m for male, f for female)",
    type=click.Choice(["m", "f"], case_sensitive=False),
    required=True,
)
def generate_name(language, gender):
    if language.lower() == "random":
        language = random.choice(["pl", "uk"])
    if language.lower() == "uk":
        if gender.lower() == "m":
            name = src.namelists.names_uk.generate_name_m_uk()
            click.echo(name)
        elif gender.lower() == "f":
            name = src.namelists.names_uk.generate_name_f_uk()
            click.echo(name)
    elif language.lower() == "pl":
        if gender.lower() == "m":
            name = src.namelists.names_pl.generate_name_m_pl()
            click.echo(name)
        elif gender.lower() == "f":
            name = src.namelists.names_pl.generate_name_f_pl()
            click.echo(name)
    else:
        click.echo("Language code not supported.")


if __name__ == "__main__":
    generate_name()
