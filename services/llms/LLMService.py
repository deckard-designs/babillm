from abc import ABC, abstractmethod

class LLMService(ABC):
    @abstractmethod
    def validateModel(self, model):
       pass

    @abstractmethod
    def query(self, model, text):
      pass