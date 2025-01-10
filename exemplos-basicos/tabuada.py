class Tabuada:
    def __init__(self, numTab):
        self.contador = 1
        self.numTab = numTab

    def calculaTab(self):
        while(self.contador <= 10):
            self.resultado = self.numTab * self.contador
            print(f"{self.contador} x {self.numTab} = {self.resultado}")
            self.contador += 1

tabuadaCalc = Tabuada(7)
tabuadaCalc.calculaTab()