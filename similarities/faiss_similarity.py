import faiss
import numpy as np

#TODO: consider more advanced indexing methods that FAISS provides, such as IndexIVFFlat, for efficiency.

def calculate_similarity(body_text_vector: np.ndarray, query_vector: np.ndarray):
    # Ensure vectors are in the right shape and type
    # Ensure the tensor is on CPU, then convert to NumPy array
    ##body_text_vector = body_text_vector.cpu().numpy()

    # Now, you can use astype as body_text_vector is a NumPy array
    body_text_vector = body_text_vector.reshape(1, -1).astype('float32')
    # Ensure the tensor is on CPU, then convert to NumPy array
    ##query_vector = query_vector.cpu().numpy()

# Now, you can use astype as query_vector is a NumPy array
    query_vector = query_vector.reshape(1, -1).astype('float32')


    # Get the dimension of the vectors
    dimension = body_text_vector.shape[1]

    # Create a FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add the body text vector to the index
    index.add(body_text_vector)

    # Search the index with the query vector
    distances, indices = index.search(query_vector, 1)

    # Return the distance
    return float(distances[0][0])

