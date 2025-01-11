# Exemplo de calculadora de IMC - Índice de Massa Corporal
class IMC:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    
    def calcular(self):
        if self.peso > 0:
            return self.peso / (self.altura ** 2)
        else:
            print("Digite um número positivo")

    def imprimir_resultado(self):
        resultado = self.calcular()
        print(f"Seu IMC é {resultado:.2f}")

novoImc = IMC(1.83, -136)
novoImc.imprimir_resultado()
