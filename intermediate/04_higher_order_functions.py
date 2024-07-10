# Higher Order Functions

from functools import reduce 

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_and_f(v1, v2, f):
    return f(v1 + v2)

print(sum_two_and_f(5, 3, sum_one))
print(sum_two_and_f(5, 3, sum_five))


# Closure

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(4))

# Built-in higher order function

numbers = [2, 5 , 12, 33]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_higher_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_higher_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Reduce 

def sum_two_values(v1, v2):
    return v1 + v2

print(reduce(sum_two_values, numbers))