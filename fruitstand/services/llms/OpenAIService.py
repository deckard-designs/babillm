from openai import OpenAI

from fruitstand.services.llms.LLMService import LLMService

class OpenAIService(LLMService):
    def __init__(self, api_key):
        self._valid_models = [
            "gpt-4o",
            "gpt-4o-mini"
        ]
        self.service = OpenAI(api_key=api_key)

    def validate_model(self, model):
        return model.lower() in self._valid_models
    
    def query(self, model, text):
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