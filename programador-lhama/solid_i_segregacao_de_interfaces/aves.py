from interfaces import AveVoadora, AveNaoVoa

class Canario(AveVoadora):
    def comer(self):
        print('Estou comendo!')

    def voar(self):
        print('Estou voando!')

    def gritar(self):
        print('Estou gritando!')

class Pinguin(AveNaoVoa):
    def comer(self):
        print('Estou comendo!')

    def gritar(self):
        print('Estou gritando!')
        self.__acasalar()

    def __acasalar(self):
        print('Agora vou acasalar')