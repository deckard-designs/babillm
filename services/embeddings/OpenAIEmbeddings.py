from services.embeddings.EmbeddingsService import EmeddingsService

class OpenAIEmbeddings(EmeddingsService):
    def __init__(self):
        self._valid_embeddings = ["text-embedding-3-large"]

    def validateEmbeddings(self, model):
        return model.lower() in self._valid_embeddings
