from abc import ABC, abstractmethod

class ElementoInterface(ABC):

    @abstractmethod
    def exec(self) -> None: pass
