from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None : pass

    @abstractmethod
    def ir_para_casa(self) -> None : pass

    @abstractmethod
    def horario_de_almoco(self) -> None : pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor está trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor está indo para casa")

    def horario_de_almoco(self) -> None:
        print("O professor está almoçando")

class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print("O engenheiro está trabalhando")

    def ir_para_casa(self) -> None:
        print("O engenheiro está indo para casa")

    def horario_de_almoco(self) -> None:
        print("O engenheiro está almoçando")

def comunicar_Trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Cominicar o trabalhado para ir para casa")
    trabalhador.ir_para_casa()

prof = Professor()
enge = Engenheiro()
comunicar_Trabalhador(prof)
print()
comunicar_Trabalhador(enge)