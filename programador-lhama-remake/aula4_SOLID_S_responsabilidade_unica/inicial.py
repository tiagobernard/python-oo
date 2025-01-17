#Princípio da Responsabilidade Única (Single Responsibility Principle)
#Princípio Aberto Fechado (Open-Closed Principle)
#Princípio da Substituição de Liskov (Liskov Substitution Principle)
#Princípio da Segregação de Interfaces (Interface Segregation Principle)
#Princípio da Inversão de Dependência (Dependency Inversion Principle)

class SistemaCadastral:

    def cadastrar(self, nome:str,idade:int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print(f"Acessando o banco de dados...")
            print(f"Cadastrar usuário {nome}, idade {idade}")
        else:
            print("dados inválidos")

