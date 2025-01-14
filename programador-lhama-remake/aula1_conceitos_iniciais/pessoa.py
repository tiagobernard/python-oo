class Pessoa:
    def __init__(self, nome: str,altura: int, idade: int) -> None:
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.atividades = ["correr", "comer"]

    def pessoa(self):
        print(f"{self.nome} gosta de {self.atividades[0]} e de {self.atividades[1]}. Ele tem {self.altura}m e {self.idade} anos de idade")

    def correr(self):
        print(f"{self.nome} está correndo")
        
    def comer(self):
        print(f"{self.nome} está comendo")

tiago = Pessoa("Tiago", 1.83, 42)
tiago.pessoa()
tiago.correr()
tiago.comer()