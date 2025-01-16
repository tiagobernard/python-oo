from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None : pass

    @abstractmethod
    def ir_para_casa(self) -> None : pass

    @abstractmethod
    def consultar_beneficios(self) -> None : pass

class TrabalhadorTemporario(ABC):

    @abstractmethod
    def trabalhar(self) -> None : pass

    @abstractmethod
    def ir_para_casa(self) -> None : pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O professor está trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor está indo para casa")

    def consultar_beneficios(self) -> None:
        print("Consultando os benefícios da CLT")

class ProfessorSubstituto(TrabalhadorTemporario):
    def trabalhar(self) -> None:
        print("O professor substituto está trabalhando")

    def ir_para_casa(self) -> None:
        print("O professor substituto está indo para casa")

p2 = ProfessorSubstituto()