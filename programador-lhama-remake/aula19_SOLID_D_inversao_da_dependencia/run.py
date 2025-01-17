#Princípio da Responsabilidade Única (Single Responsibility Principle)
#Princípio Aberto Fechado (Open-Closed Principle)
#Princípio da Substituição de Liskov (Liskov Substitution Principle)
#Princípio da Segregação de Interfaces (Interface Segregation Principle)
#Princípio da Inversão de Dependência (Dependency Inversion Principle)


from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal:
    def __init__(self, elem:ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.exec()
        print("Estou finalizando na classe principal")

el = Elemento2()
cl1 = Principal(el)
cl1.run()