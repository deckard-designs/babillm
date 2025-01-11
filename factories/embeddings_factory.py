from services.embeddings.OpenAIEmbeddings import OpenAIEmbeddings

def getEmbeddings(llm):
    if (llm == "openai"):
        return OpenAIEmbeddings()
    else:
        raise TypeError(f"{llm} is not a valid embeddings source")