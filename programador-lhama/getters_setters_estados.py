class Pessoa:
    def __init__(self, nome: str,idade: int) -> None:
        self.nome = nome #substantivo
        self.idade = idade #substantivo
    
    def dirigir(self, veiculo: str) -> None: #verbo
        print('Dirigindo um(a) {}' .format(veiculo))

    def cantar(self) -> None: #verbo
        print('lalala')

    def apresentar_idade(self) -> int: #verbo
        return self.idade