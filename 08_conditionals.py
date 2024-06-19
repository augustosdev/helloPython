# Conditionals

my_condition = True
my_age = 33
my_number = 1

if my_condition:
    print('Se ejecuta la condicion del if')

if my_age == 35:
    print('Se cumple la edad')    
else:
    print('No se cumple la edad')    

if my_number <= 12 and my_number < 50:
    print('Se cumple la condicion del numero')
elif my_number == 1: # Aunque se cumpla la condicion, no ingresa porque ya se cumple la anterior
    print('Es igual a 1')
else:
    print('No se cumplio la condicion')    

print('Continua el flujo')    
