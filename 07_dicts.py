# Diccionario

my_dict1 = dict()
print(type(my_dict1))
my_dict1 = {'name':'Augusto'}
print(my_dict1)
print(type(my_dict1))

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
