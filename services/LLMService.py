from abc import ABC, abstractmethod

class LLMService:
    @abstractmethod
    def validateModel(self, model)

    @abstractmethod
    def query(self, text):
      pass

    @abstractmethod
    def embed(self, text):
    