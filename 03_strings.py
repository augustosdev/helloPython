new_string = 'Este es un string \n con salto de linea'
print(new_string)

tab_string = '\tEste es un string con tabulacion'
print(tab_string)

# Formateo

name, surname, age = "Augusto", "Alvarado", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Dato tal como lo recibe
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))     #Dato con formato especifico
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))  #No es la forma correcta 
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  #Mejor forma para datos tal cual

# Division

language = 'Python'
language_slice = language[0:3]
print(language_slice)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo