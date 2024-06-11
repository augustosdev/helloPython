# Variables

my_string = 'hola python'
print(my_string)

my_int_variable = 14
print(my_int_variable)
print(type(my_int_variable))

# Concatenacion de variables
print(my_string, my_int_variable)

# Transformar un str a int
int_to_str = str(my_int_variable)
print(type(int_to_str))

# Variables en una sola linea (no es buena practica)
name, surname, age, alias = 'Samuel', 'Alvarado', 35, 'AugustosDev'
print('Mi nombre es: ', name, surname,)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)