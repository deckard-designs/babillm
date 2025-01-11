from abc import ABC, abstractmethod

class EmeddingsService(ABC):
    @abstractmethod
    def validate_embeddings(self, model):
        pass

    @abstractmethod
    def embed(self, model, text):
        pass