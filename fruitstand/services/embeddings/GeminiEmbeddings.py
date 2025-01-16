import google.generativeai as genai
from fruitstand.services.embeddings.EmbeddingsService import EmbeddingsService

class GeminiEmbeddings(EmbeddingsService):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

    def embed(self, model: str, text: str) -> list:
        response = genai.embed_content(
          model=model,
          content=text
        )

        # Extract the embeddings from the response
        return response["embedding"]
