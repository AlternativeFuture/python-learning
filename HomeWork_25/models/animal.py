class Animal:
    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound

    def voice(self):
        return self.__sound

