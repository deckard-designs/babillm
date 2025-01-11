from abc import ABC, abstractmethod

class EmeddingsService(ABC):
    @abstractmethod
    def validateEmbeddings(self, model):
        pass

    @abstractmethod
    def embed(self, text):
        pass