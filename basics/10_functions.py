# Functions

def my_function():
    print('Esta es una funcion')

my_function()

def sumas(numero1, numero2):
    print(numero1 + numero2)

sumas(25, 16)

def suma_return(valor1, valor2):
    return valor1 + valor2

valor_suma = suma_return(12, 24) # Se guarda en una variable el retorno
print(valor_suma)

def print_name(name, surname):
    print(f'{name} {surname}')

print_name(surname='Alvarado', name='Samuel')

def nombres(name, surname = 'n/s', age = 'sin edad'): # Se le asigna un parametro por defecto
    print(f'{name} {surname} {age}')

nombres('Samuel')

def func_parametro_libre(*texts):
    for text in texts:
        print(text.upper())

func_parametro_libre('hola', 'parametro', 'libre')