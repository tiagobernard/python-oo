class Animal:
    def alimentar(self):
        print("O animal está se alimentando")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo")

class Peixe(Cachorro):
    def nadar(self):
        print("O peixe está nadando")
    
    def latir(self):
        raise Exception("Peixe não late")

def verificar_animal(animal: any):
    animal.latir()

obj1 = Animal()
obj2 = Cachorro()
obj3 = Peixe()
verificar_animal(obj3)