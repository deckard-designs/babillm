from openai import OpenAI
from fruitstand.services.llms.LLMService import LLMService

class OpenAIService(LLMService):
    def __init__(self, api_key: str) -> None:
        self.service = OpenAI(api_key=api_key)
    
    def query(self, model: str, text: str) -> str:
        chat_completion = self.service.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ],
            model=model,
        )
        
        return chat_completion.choices[0].message.content
