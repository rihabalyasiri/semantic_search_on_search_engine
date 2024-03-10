import numpy as np

def calculate_similarity(ad_vector: list, query_vector: list):
    """
    Calculate the Euclidean distance between two vectors using NumPy.

    Parameters:
    vec1 (array-like): ad_vector.
    vec2 (array-like): query_vector.

    Returns:
    float: The Euclidean distance between vectors ad_vector and query_vector.
    """
    vec1 = np.asarray(ad_vector)
    vec2 = np.asarray(query_vector)

    # Calculate the difference between the two vectors
    diff = vec1 - vec2

    # Compute the square of the differences, sum them, and then take the square root
    distance = np.sqrt(np.sum(diff ** 2))
    print(distance)
    return float(distance)


