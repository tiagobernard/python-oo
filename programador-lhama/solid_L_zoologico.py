from typing import Type

class Animal:
    def comer(self):
        print('O animal está comendo')

    def dormir(self):
        print('O animal está dormindo')

    def andar(self):
        print('O animal estã andando')

class Aves(Animal):

    def __init__(self):
        super().__init__()
    
    def cantar(self):
        print('A ave está candando')

class Pinguin(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self):
        print('o pinguin estã escorregando no gelo')

class Pessoa:
    def observar(self, animal: type[Animal]):
        animal.comer()

roberto = Pessoa()
pinguin = Animal()
roberto.observar(pinguin)