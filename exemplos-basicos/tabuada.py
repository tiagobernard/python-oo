class Tabuada: #Classe tabuada
    def __init__(self, numTab): #método construtor
        self.contador = 1 #parâmetros
        self.numTab = numTab

    def calculaTab(self): #método
        while(self.contador <= 10):
            self.resultado = self.numTab * self.contador
            self.contador += 1
            print(f"{self.contador} x {self.numTab} = {self.resultado}")

tabuadaCalc = Tabuada(7) # Instância
tabuadaCalc.calculaTab() # chama o método calculaTab