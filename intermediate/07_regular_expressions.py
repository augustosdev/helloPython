# Expresiones regulares

import re

# Match

my_string = 'Esta es la leccion numero 7: Leccion de Expresiones regulares'
my_other_string = 'Esta no es la leccion numero 6: Manejo de ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

other_match = re.match('Esta es la leccion', my_other_string, re.I)
#if not(other_match == None): # Otra forma de comprobar el None
#if other_match != None: # Otra forma de comprobar el None
if other_match is not None:
    print(other_match)
    start, end = other_match.span()
    print(my_other_string[start:end])


# search

search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall

findall = re.findall('leccion', my_string, re.I)
print(findall)


# split

print(re.split(':', my_string))


# sub

print(re.sub('leccion|Leccion', 'LECCION', my_string))
print(re.sub('[l|L]eccion', 'LECCION', my_string))
print(re.sub('Expresiones regulares', 'RegEX', my_string))