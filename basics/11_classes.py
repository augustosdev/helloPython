# Classes

class MyPerson:
    pass

print(MyPerson)

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.fullname = f'{name} {surname} ({alias})'  # Es una propiedad Publica
        self.__name = name # Es una propiedad privada

    def get_name(self):
        return self.__name    

    def walk(self):
        print(f'{self.fullname} esta caminando')

my_person = Person('Samuel', 'Alvarado')
print(my_person.fullname)
print(my_person.get_name())
my_person.walk()