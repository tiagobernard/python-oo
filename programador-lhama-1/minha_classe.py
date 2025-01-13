class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Avançar canal')

    def voltar_canal(self):
        print('Voltar canal')

    def escolher_canal(self, canal):
        print('Alterado para o canal: {}' .format(canal))

controle_sala = ControleRemoto('Samsung', 'Sala')
print(controle_sala.comodo)
print(controle_sala.televisao)

controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('LG', 'Quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
