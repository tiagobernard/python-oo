# Vamos criar uma classe para Clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basico","premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver o filme {filme}")
        elif self.plano == "premium":
            print(f"Ver o filme {filme}")
        elif self.plano == "basico" and plano_filme == "premium":
            print("Faça o upgrade para premium para assistir esse filme.")
        else:
            print("Plano inválido")

cliente = Cliente("Tiago", "tiago@lab82.dev", "basico")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme("Herry Potter", "premium")

