import numpy as np

def cosine_similarity(vec1, vec2):
    # Convert the vectors to numpy arrays if they aren't already
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    # Compute the dot product of the two vectors
    dot_product = np.dot(vec1, vec2)
    
    # Compute the magnitude of each vector
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)
    
    # Calculate the cosine similarity
    similarity = dot_product / (magnitude_vec1 * magnitude_vec2)
    
    return float(similarity)