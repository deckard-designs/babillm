def validate(json_data):
    # Check that 'llm' is a dictionary with 'source' and 'model' as strings
    if not isinstance(json_data.get('llm'), dict):
        return False
    if not isinstance(json_data['llm'].get('source'), str) or not isinstance(json_data['llm'].get('model'), str):
        return False
    
    # Check that 'embeddings' is a dictionary with 'source' and 'model' as strings
    if not isinstance(json_data.get('embeddings'), dict):
        return False
    if not isinstance(json_data['embeddings'].get('source'), str) or not isinstance(json_data['embeddings'].get('model'), str):
        return False
    
    # Check that 'data' is a list
    if not isinstance(json_data.get('data'), list):
        return False
    
    # Check that each item in 'data' is a dictionary with 'query' and 'response' as strings, and 'vector' as a list
    for item in json_data['data']:
        if not isinstance(item, dict):
            return False
        if not isinstance(item.get('query'), str) or not isinstance(item.get('response'), str):
            return False
        if not isinstance(item.get('vector'), list):
            return False

    # If all checks pass, return True
    return True