from fruitstand.services.embeddings.OpenAIEmbeddings import OpenAIEmbeddings

def getEmbeddings(llm: str, api_key: str) -> OpenAIEmbeddings:
    if llm == "openai":
        return OpenAIEmbeddings(api_key)
    else:
        raise TypeError(f"{llm} is not a valid embeddings source")