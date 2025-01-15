from fruitstand.services.llms.OpenAIService import OpenAIService

def getLLM(llm: str, api_key: str) -> OpenAIService:
    if llm == "openai":
        return OpenAIService(api_key)
    else:
        raise TypeError(f"{llm} is not a valid embeddings llm")