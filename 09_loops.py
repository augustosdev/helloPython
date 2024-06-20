# Loop, bucle, ciclo

#Los loops sirven para iterar, osea para repetir algo una y otra vez, cuando sea necesario.

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Opcional
    print('Mi condicion es igual o mayor que 10')

print('La ejecucion continua')

while my_condition < 20:
    my_condition += 1 
    if my_condition == 15:
        print('Se detiene la ejecucion')
        break # Finaliza el bucle
    print(my_condition)

print('La ejecucion continua')

while my_condition < 30:
    my_condition += 1
    if my_condition == 24:
        print('La condicion llego a 24')
    else:
        print(my_condition)

print('La ejecucion continua')