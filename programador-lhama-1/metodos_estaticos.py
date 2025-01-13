class Error:

    @staticmethod
    def erro_500():
        print('Erro interneo do servidor')

    @staticmethod
    def erro_404():
        print('Página não encontrada')

Error.erro_500()
Error.erro_404()