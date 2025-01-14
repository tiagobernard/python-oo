from .interface import Repositorio

class MongoRepository(Repositorio):
    def inserir(self,dado) -> None:
        print('Inserirndo {} no banco Mongo' .format(dado))

    def deletar(self, dado) -> None:
        print('Removendo {} no bando Mongo' . format(dado))