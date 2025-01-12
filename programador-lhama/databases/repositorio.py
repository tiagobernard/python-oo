class Repositorio:
    def select(self, db_conection: any) -> None:
        conection = db_conection.conectar()
        print('Conectei ao BD {}' .format(conection))
        print('Fazendo um SELECT * FROM...')
        db_conection.desconectar()

    def insert(self, db_conection: any) -> None:
        conection = db_conection.conectar()
        print('Conectei ao BD {}' .format(conection))
        print('Fazendo um Insert Values...')
        db_conection.desconectar()

