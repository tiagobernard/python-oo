class Pessoa:
    def __init__(self,altura,cpf) -> None:
        self.altura = altura
        self.__cpf = cpf
    
    def apresentar (self):
        print(f"Olá! minha altura é {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f"Meu documento é {self.__cpf}")

jorge = Pessoa("1.70", "98390580782")
jorge.apresentar()