from abc import ABC, abstractmethod

class serivceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass