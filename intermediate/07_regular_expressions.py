# Expresiones regulares

import re

# Match

my_string = 'Esta es la leccion numero 7: Expresiones regulares'
my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)