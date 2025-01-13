import logging

from fruitstand.controllers import baseline

class Fruitstand:
    def __init__(self):    
      logging.basicConfig(level=logging.INFO)
      logging.getLogger("http").setLevel(logging.WARNING)
      logging.getLogger("httpx").setLevel(logging.WARNING)
      
  
    def baseline(
        query_llm, 
        query_api_key, 
        query_model, 
        embeddings_llm, 
        embeddings_api_key, 
        embeddings_model,
        output_directory
    ):
        baseline.start(
            filename, 
            query_llm, 
            query_api_key, 
            query_model, 
            embeddings_llm, 
            embeddings_api_key, 
            embeddings_model,
            output_directory
        )
       
      