import numpy as np
from scipy.linalg import block_diag

def block_matrix(matrix_list):
    """Takes in a list of square matrices and arranges them into a block-diagonal form"""

    #calling the block_diag function from scipy.linalg and prints out the result
    return block_diag(*matrix_list)

def main():
    block_matrix([np.array([[2, 3], [4, 5]]), np.array([[9, 4, 1], [10, 2, 0], [6, 3, 7]]), np.array([[1, 0], [0, 1]])])

if __name__ == "__main__":
    main()