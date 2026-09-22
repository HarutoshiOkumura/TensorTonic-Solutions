import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    result = 0.0
    for idx in range(len(x)): 
        result += x[idx] * y[idx]
    return result