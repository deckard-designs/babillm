from openai import OpenAI
from fruitstand.services.embeddings.EmbeddingsService import EmbeddingsService

class OpenAIEmbeddings(EmbeddingsService):
    def __init__(self, api_key: str):
        self.service = OpenAI(api_key=api_key)

    def embed(self, model: str, text: str) -> list:
        response = self.service.embeddings.create(
            model=model,  # set the model for embeddings
            input=text
        )

        # Extract the embeddings from the response
        return response.data[0].embedding
