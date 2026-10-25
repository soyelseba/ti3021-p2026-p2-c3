import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

class Mascota:
    def __init__(self, nombre: str,
                especie: str, peso: float,
                id: int | None = None):
        self.__id = id
        self.__nombre = nombre
        self.__especie = especie
        self.__peso = peso

    def obtenerId(self): return self.__id
    def obtenerNombre(self): return self.__nombre
    def obtenerEspecie(self): return self.__especie
    def obtenerPeso(self): return self.__peso

class ConexionOracle:
    def __init__(self, user, password, dsn):
        self.__user = user
        self.__password = password
        self.__dsn = dsn

    def abrir(self):
        return oracledb.connect(
            user=self.__user,
            password=self.__password,
            dsn=self.__dsn
        )

    def crear(self, mascota: Mascota) -> int:
        sql = """INSERT INTO mascota
        (nombre, especie, peso)
        VALUES (:nombre, :especie, :peso)
        RETURNING id INTO :id"""

        with self.abrir() as con:
            with con.cursor() as cur:
                nuevo_id = cur.var(int)
                cur.execute(sql, nombre=mascota.obtenerNombre(),
                especie=mascota.obtenerEspecie(),
                peso=mascota.obtenerPeso(), id=nuevo_id)
                con.commit()
                return nuevo_id.getvalue()[0]

config = ConexionOracle(
    user=os.getenv("user"), 
    password=os.getenv("password"), 
    dsn=os.getenv("dsn") 
)

mascota_1 = Mascota(
    nombre="Lucas",
    especie="Gallus gallus domesticus",
    peso=0.370,
    id=1
)

print(config.crear(mascota=mascota_1))
