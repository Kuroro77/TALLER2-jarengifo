
class Perro:
    def __init__(self, nombre:str, edad:int, raza:str, peso:float, concentrado:str = 'No elegido')->None:
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        self.__concentrado = concentrado

    def hacer_sonido(self) -> str:
        return "¡Guau Guau!"


