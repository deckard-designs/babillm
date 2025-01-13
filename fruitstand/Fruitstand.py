import logging

from fruitstand.controllers import baseline, test

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
        data
    ):
        return baseline.start(
            query_llm, 
            query_api_key, 
            query_model, 
            embeddings_llm, 
            embeddings_api_key, 
            embeddings_model,
            data
        )
    
    def test(
        test_query_llm,
        test_query_api_key,
        test_query_model,
        embeddings_api_key,
        success_threshold,
        baseline_data,
        test_data
    ):
        return test.start(
            test_query_llm,
            test_query_api_key,
            test_query_model,
            embeddings_api_key,
            success_threshold,
            baseline_data,
            test_data
        )
       
      