# Python Package Manager

#PIP  https://pypi.org/

import numpy        #pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([12, 23, 15, 33, 35])
print(type(numpy_array))

import pandas       #pip install pandas

# pip list
# pip unistall pandas
# pip show numpy

import requests 

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetic package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))


