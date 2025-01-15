from abc import ABC, abstractmethod

class Pessoa(ABC): # Classe abstrata não possui objetos - só pode ser mãe
    def correr(self):
        print("A pessoa está correndo de manhã")

    @abstractmethod #A Classe filha deve criar um método trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("o professor está dando aula")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O Cozinheiro está cozinhando")

prof1 = Professor()
prof1.trabalhar()
prof1.correr()
print()
coz1 = Cozinheiro()
coz1.trabalhar()
coz1.correr()