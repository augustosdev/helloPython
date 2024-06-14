# Sets

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Augusto", "Alvarado", 35}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("Augustosdev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Augustosdev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Augusto" in my_other_set)
print("Augustos" in my_other_set)

# Eliminación

my_other_set.remove("Alvarado")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Augusto", "Alvarado", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))