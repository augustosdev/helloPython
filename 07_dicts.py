'''# Diccionario

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


# Agregar

my_dict['Lenguajes'].add('js')

print(my_dict)

my_dict['Lenguajes'].add('JavaScript')

print(my_dict)

# Renombrar

my_dict["Apellido"] = 'Alvarados'

print(my_dict["Apellido"])

# Busqueda

print(my_dict["Nombre"])
print(my_dict["Lenguajes"])

print('Samuel' in my_dict)
print('Augusto' in my_dict)
print('Nombre' in my_dict)
print('nombre' in my_dict)
'''

my_directorio = {'nombre':'Jose', 'mail':'jose@gmail.com', 'herramientas':{'martillo', 'escalera'}}
print(my_directorio)

print(my_directorio.fromkeys(("nombre", 'mail')))

new_directorio = my_directorio.fromkeys(('nombre', 'mail'))
print(new_directorio)

print(my_directorio)

my_new_dict = dict.fromkeys((new_directorio))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))