class Mae:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo')

    def estudar(self) -> None:
        print('Estou estudando')

class Filha(Mae):
    def __init__(self, endereco):
        super().__init__(endereco)

    def brincar(self, brinquedo: str) -> None:
        print('Estou brincando com {}' .format(brinquedo))

class Neta(Filha):
    def __init__(self, endereco):
        super().__init__(endereco)

ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')
alice = Neta('Rua Francisco')
clara.brincar('Boneca')

print(ana.endereco)
print(clara.endereco)
print(alice.endereco)