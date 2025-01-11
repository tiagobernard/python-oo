# Exemplo de calculadora de IMC - Índice de Massa Corporal
class IMC: #classe que encapsula dados e métodos
    def __init__(self, altura, peso): #método construtor
        self.altura = altura #atributos
        self.peso = peso
    
    def calcular(self): #método de que calcula o IMC
        if self.peso > 0 and self.altura > 0: #Testa se o peso e altura são negativos
            return self.peso / (self.altura ** 2) # Se verdadeiro retorna o cálculo do IMC
        else:
            raise ValueError("Digite um número positivo") # lança uma exceção, se falso retorna uma mesagem de erro

    def imprimir_resultado(self): #método que mostra o IMC ou mnsagem de erro
        try: #inicia um bloco de código que pode gerar uma exceção
            resultado = self.calcular() #chama o método calcular
            print(f"Seu IMC é {resultado:.2f}") # mensagem com o resultado do IMC com duas casas decimais
        except ValueError as e: #Captura a exceção lançada pelo método calcular para obter o IMC
            print(e) # imprime a mensagem de erro capturada

novo_imc = IMC(1.83, 136)  # Instância da Classe IMC
novo_imc.imprimir_resultado() # chama o método que imprime os resultado da instância novo_imc ou erro