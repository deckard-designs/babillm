from openai import OpenAI

from fruitstand.services.embeddings.EmbeddingsService import EmeddingsService

class OpenAIEmbeddings(EmeddingsService):
    def __init__(self, api_key):
        self._valid_embeddings = ["text-embedding-3-large"]
        self.service = OpenAI(api_key=api_key)

    def validate_embeddings(self, model):
        return model.lower() in self._valid_embeddings

    def embed(self, model, text):
        response = self.service.embeddings.create(
            model=model,  # set the model for embeddings
            input=text
        )

        # Extract the embeddings from the response
        return response.data[0].embedding