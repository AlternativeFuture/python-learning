from models.animal import Animal


class Dog(Animal):

    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.__color = color

    def get_color(self):
        return self.__color

