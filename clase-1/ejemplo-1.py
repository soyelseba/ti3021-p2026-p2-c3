# Un docente necesita clasificar el 
# rendimiento de un estudiante a partir 
# de tres calificaciones en escala de 1,0 a 7,0.

"""
------------------------------------------
|               Estudiante               |
|----------------------------------------|
| - nombre: str                          |
| - notas: list<<float>>                 |
| - / promedio: float                    |
| - / clasificacion: str                 |
|----------------------------------------|
| - calcularPromedio(notas): float       |
| - calcularClasificacion(promedio): str |
| + mostrarResumen(): void               |
------------------------------------------
""" 

class Estudiante:
    def __init__(self, nombre: str, notas: list[float]):
        self.__nombre: str = nombre
        self.__notas: list[float] = notas
        self.__promedio: float = self.__calcularPromedio(self.__notas)
        self.__clasificacion: str = self.__calcularClasificacion(self.__promedio)

    def __calcularPromedio(self, notas: list[float]) -> float:
        return round(sum(notas) / len(notas), 2)
    
    def __calcularClasificacion(self, promedio: float) -> str:
        if promedio < 4.0: return "Reprobado"
        elif promedio >= 4.0 and promedio <= 4.94: return "Aprobado"
        elif promedio >= 5.0 and promedio <= 5.94: return "Buen rendimiento"
        elif promedio >= 6.0 and promedio <= 7.0: return "Rendimiento destacado"

    def mostrarResumen(self):
        print("Estudiante:", self.__nombre)
        print("Promedio:", self.__promedio)
        print("Clasificacion", self.__clasificacion)

nombre = input("Ingrese el nombre del estudiante: ")

def pedir_nota(posicion: str) -> float:
    nota: float = float( input(f"Ingrese la {posicion} nota del estudiante: ") )
    while not 1.0 < nota < 7.0:
        print("La nota debe de estar entre 1.0 y 7.0")
        nota: float = float( input(f"Ingrese {posicion} la nota del estudiante: ") )
    return nota

primera_nota = pedir_nota(posicion="primera")
segunda_nota = pedir_nota(posicion="segunda")
tercera_nota = pedir_nota(posicion="tercera")

estudiante_1 = Estudiante(nombre=nombre, notas=[primera_nota, segunda_nota, tercera_nota])
estudiante_1.mostrarResumen()