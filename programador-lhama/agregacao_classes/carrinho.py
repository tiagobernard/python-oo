from produtos import Produto
from servicos import Servico
from typing import Type

class CarrinhoDeCompras:

    def __init__(self) -> None:
        self.__produtos = []
        self.__servicos = []

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def adicionar_servico(self, servico: Type[Servico]) -> None:
        self.__servicos.append(servico)

    def finalizar_compra(self) -> None:
        print('Compras finalizadas')

        for produto in self.__produtos:
            produto.informacoes_produto()
            self.__produtos = []

        for servico in self.__servicos:
            servico.informacoes_servico()
            self.__produtos = []