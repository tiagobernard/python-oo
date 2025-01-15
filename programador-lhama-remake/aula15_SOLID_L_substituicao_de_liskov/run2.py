class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco")

class SqlRepository():
    def select(self):
        print("Bscando dados no banco SQL")

class NoSqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco de daodos NoSql")

class DBHandler:
    def alterTable(self):
        print("Alternado tabela em SQL")