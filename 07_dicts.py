# Diccionario

my_diccionario = dict()
print(type(my_diccionario))
my_diccionario = {'name':'Augusto'}
print(my_diccionario)
print(type(my_diccionario))

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Augusto",
                 "Apellido": "Alvarado", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Augusto",
    "Apellido": "Alvarado",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.69
}

print(my_other_dict)
print(my_dict)

my_dict['Lenguajes'].add('js')

print(my_dict)

my_dict['Lenguajes'].add('JavaScript')

print(my_dict)