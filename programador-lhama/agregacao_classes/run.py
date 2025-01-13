from produtos import Produto
from servicos import Servico
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
agua = Produto('Água Mineral', 2)
tv = Produto('TV', 2000)
car.adicionar_produto(monitor)
car.adicionar_produto(agua)
car.adicionar_produto(tv)
manutencao = Servico('Manutenção técnica', 275)
host = Servico('Hospedagem Dedicada', 697)
car.adicionar_servico(manutencao)
car.adicionar_servico(host)

car.finalizar_compra()