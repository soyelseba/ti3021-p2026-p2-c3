# Abstraccion
# La capacidad de reconocer las partes más
# importantes para un sistema informático.

# Clase -> Plantilla
# Visibilidad, Nombre Atributo y Tipo de dato
# Visibilidad, Nombre Metodo, Argumentos y Tipo de dato retornado

# Definir una Mascota
# **** LOS NOMBRES DE LAS CLASES VAN EN SINGULAR
# ----------> Mascota : OK
# ----------> Mascotas : MALO

"""
------------------------------------------
|               Mascota                  |
|----------------------------------------|
| + nombre: str                          |
| + edad: str                            |
| + especie: str                         |
| + color_pelaje: str                    |
| + raza: str                            |
| + peso: float                          |
| + sexo: str                            |
| + fallecido: bool                      |
| + estado: str                          |
|----------------------------------------|
|                                        |
------------------------------------------
""" 

class Mascota:
    def __init__(self, 
        nombre: str, 
        edad: str, 
        especie: str, 
        color_pelaje: str, 
        raza: str, 
        peso: float, 
        sexo: str, 
        fallecido: bool, 
        estado: str
    ):
        self.nombre: str = nombre
        self.edad: str = edad
        self.especie: str = especie
        self.color_pelaje: str = color_pelaje
        self.raza: str = raza
        self.peso: float = peso
        self.sexo: str = sexo
        self.fallecido: bool = fallecido
        self.estado: str = estado