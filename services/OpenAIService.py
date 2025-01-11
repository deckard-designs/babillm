class OpenAIService:
    def __init__(self):
        self._valid_models = ["gpt-3.5 turbo"]

    def validateModel(self, model):
        return model.lower() in self._valid_models