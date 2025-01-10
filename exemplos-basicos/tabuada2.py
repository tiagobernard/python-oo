class Tabuada: #classe
    def __init__(self, numTab): #método construtor
        self.numTab = numTab #atributo

    def calculaTab(self): #método de cálculo da tabuada
        resultados = []
        for contador in range(1,11):
            resultado = self.numTab * contador
            resultados.append((contador, resultado))
        return resultados
    
    def imprimeResultados(self, resultados): #método que imprime os resultados
        for contador, resultado in resultados:
            print(f"{contador} x {self.numTab} = {resultado}")

tabuadaCalc = Tabuada(7) #instância da classe Tabuada
resultados = tabuadaCalc.calculaTab() #cálculo dos resultados
tabuadaCalc.imprimeResultados(resultados) # imprime os resultados