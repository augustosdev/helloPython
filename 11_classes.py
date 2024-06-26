# Classes

class MyPerson:
    pass

print(MyPerson)

class Person:
    def __init__(self, name, surname):
        self.fullname = f'{name} {surname}'

    def walk(self):
        print(f'{self.fullname} esta caminando')

my_person = Person('Samuel', 'Alvarado')
print(my_person.fullname)
my_person.walk()