from abc import ABC, abstractmethod

class LLMService(ABC):
   @abstractmethod
   def query(self, model: str, text: str) -> str:
      pass