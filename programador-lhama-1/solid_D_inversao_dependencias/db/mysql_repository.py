from .interface import Repositorio

class MysqlRepositorio(Repositorio):
    def inserir(self,dado) -> None:
        print('Inserirndo {} no banco Mysql' .format(dado))

    def deletar(self, dado) -> None:
        print('Removendo {} no bando Mysql' . format(dado))