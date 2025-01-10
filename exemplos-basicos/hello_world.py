#Hello World!

class HelloWorld:
    def __init__(self, menssagem):
        self.menssagem = menssagem

    def mostrar_mensagem(self):
        print(self.menssagem)

#Criando uma instância da classe HelloWorld
hello = HelloWorld("Hello, World!")
hello.mostrar_mensagem()