#SOLID
# S = Responsabilidade única = Single responsability

class SistemaCadastral:

    def cadastrar(self, nome:str,idade:int) -> None:
        if self.__validade_input(nome,idade):
            self.__register_user(nome,idade)
        else:
            print("dados inválidos")

    def __validade_input(self, nome: str, idade:int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome:str,idade:int) -> None:
        print(f"Acessando o banco de dados...")
        print(f"Cadastrar usuário {nome}, idade {idade}")

    def __error_handle(self) -> None:
        print("Dados inválidos")

sistema = SistemaCadastral()
sistema.cadastrar("Tiago", 42)