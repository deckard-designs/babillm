import google.generativeai as genai
from fruitstand.services.llms.LLMService import LLMService

class GeminiService(LLMService):
    def __init__(self, api_key: str) -> None:
        genai.configure(api_key=api_key)
    
    def query(self, model: str, text: str) -> str:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(text)

        return response.text
