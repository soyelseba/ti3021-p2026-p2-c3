# Encapsulamiento
# Mecanismo de proteccion
# a los atributos y metodos de la clase

# Getter()
# Metodo publico para obtener informacion

# Setter()
# Metodo publico para modificar informacion

"""
------------------------------------------
|               Mascota                  |
|----------------------------------------|
| - nombre: str                          |
| - edad: str                            |
| - especie: str                         |
| - color_pelaje: str                    |
| - raza: str                            |
| - peso: float                          |
| - sexo: str                            |
| - fallecido: bool                      |
| - estado: str                          |
|----------------------------------------|
| + obtener_nombre(): str                |
| + obtener_edad(): str                  |
| + obtener_especie(): str               |
| + obtener_color_pelaje(): str          |
| + obtener_raza(): str                  |
| + obtener_peso(): float                |
| + obtener_sexo(): str                  |
| + obtener_fallecido(): bool            |
| + obtener_estado(): str                |
| + establecer_peso(nuevo_peso): void    |
------------------------------------------ 
""" 

class Mascota:
    def __init__(self, nombre: str, edad: str, especie: str, color_pelaje: str, raza: str, peso: float, sexo: str, fallecido: bool, estado: str):
        self.__nombre: str = nombre
        self.__edad: str = edad
        self.__especie: str = especie
        self.__color_pelaje: str = color_pelaje
        self.__raza: str = raza
        self.__peso: float = peso
        self.__sexo: str = sexo
        self.__fallecido: bool = fallecido
        self.__estado: str = estado

    def obtener_nombre(self) -> str: return self.__nombre
    def obtener_edad(self) -> str: return self.__edad
    def obtener_especie(self) -> str: return self.__especie
    def obtener_color_pelaje(self) -> str: return self.__color_pelaje
    def obtener_raza(self) -> str: return self.__raza
    def obtener_peso(self) -> float: return self.__peso
    def obtener_sexo(self) -> str: return self.__sexo
    def obtener_fallecido(self) -> bool: return self.__fallecido
    def obtener_estado(self) -> str: return self.__estado

    def establecer_peso(self, nuevo_peso: float): 
        if nuevo_peso <= 0: return print("La mascota no puede pesar ni 0 ni menos que 0.")
        else:
            self.__peso = nuevo_peso
            print("Nuevo peso establecido para la mascota.")