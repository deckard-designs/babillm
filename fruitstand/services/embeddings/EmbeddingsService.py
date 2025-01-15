from abc import ABC, abstractmethod
from typing import Any

class EmbeddingsService(ABC):
    @abstractmethod
    def embed(self, model: Any, text: str) -> list:
        pass