# Modules

import my_module # Importa el modulo completo

my_module.sumas(2, 5)
my_module.print_test('Funciona Print text')


from my_module import sumas, print_test

sumas(12, 3)
print_test('Funciona el import')

import math 
 
print(math.pi)
print(math.pow(2,8))

from math import pi as pi_value # Renombrando PI

print(pi_value)
