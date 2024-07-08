# Lambdas

suma = lambda num_uno, num_dos: num_uno + num_dos

print(suma(5, 2))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))