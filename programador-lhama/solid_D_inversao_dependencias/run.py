from typing import Type
from db.interface import Repositorio
from db.mongo_repository import MongoRepository
from db.mysql_repository import MysqlRepositorio

class Usuario:
    def __init__(self, respositorio: Type[Repositorio]) -> None:
        self.__repositorio = respositorio

    def armazenar_dados(self, dado:any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dados(self, dado:any) -> None:
        self.__repositorio.deletar(dado)

usuariomysql = Usuario(MysqlRepositorio())
usuariomysql.armazenar_dados(23)

usuariomongo = Usuario(MongoRepository())
usuariomongo.armazenar_dados(25)