from fruitstand.services.embeddings.GeminiEmbeddings import GeminiEmbeddings
from fruitstand.services.embeddings.OpenAIEmbeddings import OpenAIEmbeddings

def getEmbeddings(llm: str, api_key: str) -> OpenAIEmbeddings:
    if llm == "openai":
        return OpenAIEmbeddings(api_key)
    if llm == "gemini":
        return GeminiEmbeddings(api_key)
    else:
        raise TypeError(f"{llm} is not a valid embeddings source")