from models.animal import Animal


class Cat(Animal):

    def __init__(self, name, sound, age):
        super().__init__(name, sound)
        self.__age = age

    def get_age(self):
        return self.__age

