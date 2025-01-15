class Mamifero:
    def __init__(self, localizacao:str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f"O animal está andando pelo {self.localizacao}")

class Cachorro(Mamifero):
    def __init__(self, localizacao:str):
        super().__init__(localizacao) #se refere ao construtor da classe superior
    def latir(self) -> None:
        print("O cachorro está latindo")
        self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao):
        super().__init__(localizacao)
    
    def miar(self) -> None:
        print("O gato está miando")

dog = Cachorro("Chile")
dog.latir()

cat = Gato("Noruega")
cat.miar()