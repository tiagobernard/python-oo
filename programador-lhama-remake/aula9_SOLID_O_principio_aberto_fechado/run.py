class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo
    
    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando seu show")

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print("O circo está abrindo")
        artista.apresentar_show()
        print("o público aplaude!")

circo = Circo()
palhaco = Artista("Palhaço")
magico = Artista("Mágico")
malabarista = Artista("Malabarista")

circo.apresentar(malabarista)