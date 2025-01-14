class MinhaClasse:

    def __init__(self,info,elemento): #método construtor
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elemento
        self.atributo_3 = [1,2,"a"]
        self.atributo_novo = info
        print(self.atributo_novo)
        
    def metodo1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo_2)
        return "Olá Mundo"

    def metodo2(self, numero):
        print(self.atributo_3[1] + numero)
        self.metodo1()

# objeto / classe = instaciamos um objeto
minha_classe = MinhaClasse("info aqui no contrutor",213)
minha_classe.metodo2(3)