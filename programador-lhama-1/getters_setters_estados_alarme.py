class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor

al = Alarme(False)
print(al.get_estado())
al.set_estado(True)
print(al.get_estado())