from services.llms.OpenAIService import OpenAIService

def getLLM(llm):
    if (llm == "openai"):
        return OpenAIService()
    else:
        raise TypeError(f"{llm} is not a valid embeddings llm")