class DatabaseConn:
    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connetion(self) -> None:
        print('Connection OK!')

class Repository(DatabaseConn):
    def __init__(self) -> None:
        super().__init__()
        #print(self.user)
        #print(self.__database)
       #print(self._conn)

    def select(self) -> None:
        self._testing_connetion()
        print('Connecting to {}' .format(self._conn))
        print('SELECT * FROM table')

repo = Repository()
repo.select()