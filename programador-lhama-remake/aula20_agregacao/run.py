class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor
    
    def informacoes_produto(self) -> None:
        print(f"Produto: {self.__nome} - Valor: {self.__valor}")

class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Produto) -> None:
        self.__produtos.append(produto)
    
    def finalizar_compra(self) -> None:
        print("Compra finalizada")
        print("     Produtos: ")
        for product in self.__produtos:
            product.informacoes_produto()


banana = Produto("Banana", 3)
pera = Produto("Pera", 2)
uva = Produto("Uva", 4)

carrinho = CarrinhoCompras()
carrinho.adicionar_produtos(banana)
carrinho.adicionar_produtos(pera)
carrinho.adicionar_produtos(uva)

carrinho.finalizar_compra()