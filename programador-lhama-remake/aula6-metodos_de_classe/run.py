class MinhaClasse:
    estatico = "lhama"

    def __init__(self, estado):
        self.__estado = estado

    def print_variavel_classe(self):
        print(self.estatico)

    @classmethod
    def alteracao_variavel_classe(cls):
        cls.estatico = "Alguma coisa"
        # MinhaClasse.estatico = "Alguma coisa"
    
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj1.alteracao_variavel_classe()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)