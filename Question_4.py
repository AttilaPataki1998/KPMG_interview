import numpy as np

def rowwise_norm(vectors):
    """Calculates the L2 norm of every row in a 2D array"""

    #squaring the 2D arrays
    squared = vectors * vectors

    #summing up the square values, axis=-1 sums up the rows
    norms = np.sqrt(np.sum(squared, axis=-1))

    #returns an array, where each row contains the norm of the rows of the original array
    return np.reshape(norms, (len(norms), 1))

def main():
    rowwise_norm(np.array([[3, 4], [6, 8]]))

if __name__ == "__main__":
    main()