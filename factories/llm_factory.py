from services.OpenAIService import OpenAIService

def getLLM(llm):
    if (llm == "openai"):
        return OpenAIService()