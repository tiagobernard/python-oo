class PessoaA:
    def se_apresentar(self):
        print('Olá, sou a pessoa A')

class PessoaB(PessoaA):
        def __init__(self):
             super().__init__()

        def se_apresentar(self):
            print('Estou alterando esse método')

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()