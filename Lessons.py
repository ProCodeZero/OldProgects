# Классы

class Person:
    # Конструктор
    def __init__(self, name,):
        self.name = name    # Имя человека
        self.age = 1      # Возраст человека

    def display_info(self):
        print(f'Name: {self.name}  \nAge: {self.age}')


tom = Person('Tom')
tom.display_info()