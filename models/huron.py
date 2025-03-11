
class Huron():
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"
