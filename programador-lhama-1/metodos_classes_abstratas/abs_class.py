from abc import ABC, abstractmethod

class AbstractClass: #(ABC)

    def __init__(self):
        self.atributo = "Olá Mundo"

    def metodo(self,elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass