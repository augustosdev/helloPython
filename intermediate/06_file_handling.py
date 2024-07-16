# Manejo de ficheros

import os

# .txt file

txt_file = open('intermediate/my_file.txt', 'w+') 

txt_file.write('Mi nombre es Samuel\nMi apellido Alvarado\ntengo 35\nestoy aprendiendo Python')

#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write('\nAunque tambien me gusta JS')
print(txt_file.readline())

txt_file.close()

with open('intermediate/my_file.txt', 'a') as  my_other_file:
    my_other_file.write('\nY SQL')

#os.remove('intermediate/my_file.txt')


# Json file

import json

json_file = open('intermediate/my_file.json', 'w+')

json_test ={
    'name' : 'Samuel',
    'surname' : 'Alvarado',
    'age' : 35,
    'languages' : ['Python', 'Swift', 'JS'],
    'website' : 'https://augustos.dev' 
}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open('intermediate/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('intermediate/my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])


# .csv file

import csv

csv_file = open('intermediate/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Samuel', 'Alvarado', 35, 'Python', 'https://augustos.dev'])
csv_writer.writerow(['Augusto', '', 2, '', 'https://augustos.dev'])

csv_file.close()

with open('intermediate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)



# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

import xml


