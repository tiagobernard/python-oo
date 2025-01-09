class Cachorro:
    def __init__(self, nome, comida, sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono

    #Definindo o método dentro da classe Cachorro
    def exibir_atributos(self):
        print(f"Nome do Cachorro: {self.nome}")
        print(f"Quantidade de comida: {self.comida}")
        print(f"Está dormindo? {'Sim' if self.sono else 'Não'}")

#Criando uma instância da classe Cachorro
cachorro_rex = Cachorro("Rex", 5, True)
cachorro_aristides = Cachorro("Aristides", 3, False)

#Chamando o método exibir_atributos para imprimir os atributos
cachorro_rex.exibir_atributos()
print(f"----------------------")
cachorro_aristides.exibir_atributos()