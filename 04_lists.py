###  LISTAS  ###

my_list = list()

my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 30, 30, 15]

print(my_list)

my_other_list = [35, 1.69, 'Samuel', 'Augusto']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[1])
print(my_other_list[-1])

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])