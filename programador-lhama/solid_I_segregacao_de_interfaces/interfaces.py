from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'
    
    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'
    
    def gritar(self):
        raise 'Should implement gritar method'
    

class AveNaoVoa(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'
    
    def gritar(self):
        raise 'Should implement gritar method'