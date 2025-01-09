class Cachorro:
    def __init__(self, nome, comida, sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono

    def set_nome(self):
        self.nome = "Aristides"
    
    def comer(self):
        self.comida -= 1

    def dormir(self):
        self.sono = False

#Criando uma instância da classe Cachorro
cachorro_rex = Cachorro("Rex", 5, True)

#Imprindo os atributos da classe Cachorro
print(f"Nome do cachorro: {cachorro_rex.nome}")
print(f"Quantidade de comida: {cachorro_rex.comida}")
print(f"O cachorro está dormindo? {'Sim' if cachorro_rex.sono else 'Não'}")