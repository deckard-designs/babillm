import anthropic 
from fruitstand.services.llms.LLMService import LLMService

class AnthropicService(LLMService):
    def __init__(self, api_key: str) -> None:
        self.service = anthropic.Anthropic(api_key=api_key)
    
    def query(self, model: str, text: str) -> str:
        chat_completion = self.service.messages.create(
            model=model,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ],
        )

        return chat_completion.content[0].text
