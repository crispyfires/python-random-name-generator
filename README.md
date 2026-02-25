# python-random-name-generator
 Generates a random name from a pre-defined wordlist on the CLI. Has options to specify number of names, language of origin, and gender using command-line arguments. 

 Arguments:
Usage: gen [OPTIONS]

Options:
  --language TEXT   Specifies which language (in 2-digit ISO 639 codes) the
                    name should come from. Use 'random' for random selection.
                    Default is 'random'
  --number INTEGER  Specifies amount of names outputted (in numerals). Default
                    is '1'
  --gender [m|f]    Specifies the gender of the name (m for male, f for
                    female)  [required]
  --help            Show this message and exit.
