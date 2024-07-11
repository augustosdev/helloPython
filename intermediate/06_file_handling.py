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



