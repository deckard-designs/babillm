import logging
from typing import List, Dict, Any

from fruitstand.controllers import baseline, test

class Fruitstand:
    def __init__(self):    
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("http").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)
      
    def baseline(
        self,
        query_llm: str, 
        query_api_key: str, 
        query_model: str, 
        embeddings_llm: str, 
        embeddings_api_key: str, 
        embeddings_model: str,
        test_data: List[Dict[str, Any]]
    ) -> dict:
        return baseline.start(
            query_llm, 
            query_api_key, 
            query_model, 
            embeddings_llm, 
            embeddings_api_key, 
            embeddings_model,
            test_data
        )
    
    def test(
        self,
        test_query_llm: str,
        test_query_api_key: str,
        test_query_model: str,
        embeddings_api_key: str,
        success_threshold: float,
        baseline_data: dict,
        test_data: List[Dict[str, Any]]
    ) -> dict:
        return test.start(
            test_query_llm,
            test_query_api_key,
            test_query_model,
            embeddings_api_key,
            success_threshold,
            baseline_data,
            test_data
        )
