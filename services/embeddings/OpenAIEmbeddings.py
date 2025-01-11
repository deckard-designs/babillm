from openai import OpenAI

from services.embeddings.EmbeddingsService import EmeddingsService

class OpenAIEmbeddings(EmeddingsService):
    def __init__(self, api_key):
        self._valid_embeddings = ["text-embedding-3-large"]
        self.service = OpenAI(api_key)

    def validateEmbeddings(self, model):
        return model.lower() in self._valid_embeddings

    def embed(self, model, text):
        embeddings = self.openai.Embedding.create(
            model=model,  # Choose the model for embeddings
            input=text
        )

        # Extract the embeddings from the response
        return embeddings['data']