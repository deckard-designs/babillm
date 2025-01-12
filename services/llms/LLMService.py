from abc import ABC, abstractmethod

class LLMService(ABC):
   @abstractmethod
   def validate_model(self, model):
      pass

   @abstractmethod
   def query(self, model, text):
      pass