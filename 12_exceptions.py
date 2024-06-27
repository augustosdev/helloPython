# Manejo de exepciones

number_one = 5
number_two = 2

#number_two = '2'

# Try except

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error')


# Try except else finally

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')
finally:
    # Se ejecuta siempre
    print('La ejecucion continua')
