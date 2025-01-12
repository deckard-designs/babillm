from fruitstand.services.embeddings.OpenAIEmbeddings import OpenAIEmbeddings

def getEmbeddings(llm, api_key):
    if (llm == "openai"):
        return OpenAIEmbeddings(api_key)
    else:
        raise TypeError(f"{llm} is not a valid embeddings source")