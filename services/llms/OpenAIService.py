from openai import OpenAI

from services.llms import LLMService

class OpenAIService(LLMService):
    def __init__(self, api_key):
        self._valid_models = ["gpt-3.5 turbo"]
        self.service = OpenAI(api_key)

    def validateModel(self, model):
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