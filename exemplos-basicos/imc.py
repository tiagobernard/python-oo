# Exemplo de calculadora de IMC - Índice de Massa Corporal
class IMC:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso
    
    def calcular(self):
        if self.peso > 0:
            return self.peso / (self.altura ** 2)
        else:
            raise ValueError("Digite um número positivo")

    def imprimir_resultado(self):
        try:
            resultado = self.calcular()
            print(f"Seu IMC é {resultado:.2f}")
        except ValueError as e:
            print(e)

novo_imc = IMC(1.83, -136)  # Isso agora levantará uma exceção
novo_imc.imprimir_resultado()