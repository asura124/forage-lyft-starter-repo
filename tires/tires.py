from abc import ABC, abstractmethod

class tires(ABC):
    @abstractmethod
    def needs_service(self):
        pass