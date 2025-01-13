class Servico:

    def __init__(self, serv_nome: str, serv_valor: int) -> None:
        self.__serv_nome = serv_nome
        self.__serv_valor = serv_valor

    def informacoes_servico(self) -> None:
        print('Serviço: {} / valor: R$ {},00' .format(self.__serv_nome, self.__serv_valor))