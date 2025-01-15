class Mamifero:
    def __init__(self, localizacao:str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f"O animal está andando pelo {self.localizacao}")

    def _dormir(self) -> None: #metodo protegido
        print("O animal está dormindo")

class Gato(Mamifero):
    def __init__(self, localizacao: str):
        super().__init__(localizacao)
    
    def miar(self) -> None:
        print("O gato está miando")
        self._dormir()
        print(self._tamanho)

cat = Gato("Argentina")
cat.miar()
cat._dormir() #deveria dar erro em outras linguagens / elementos protegidos não são chamados por objetos
print(cat._tamanho) #elementos protegidos não são chamados por objetos