#Hello World!

class HelloWorld:
    def __init__(self, message):
        self.message = message

    def display_message(self):
        print(self.message)

#Criando uma instância da classe HelloWorld
hello = HelloWorld("Hello, World!")
hello.display_message()