class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('Malabarista Apresentando seu show')

class Palhaco:
    def apresentar_show(self):
        print('Palhaço Apresentando seu show')

class Magico:
    def apresentar_show(self):
        print('Mágico Apresentando seu show')

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
magico = Magico()

circo.apresentar(magico)