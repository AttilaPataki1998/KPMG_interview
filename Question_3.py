import numpy as np

def chessboard(n):
    """Creates an array with a chessboard like pattern of 1s and -1s"""

    #an nxn 2D array of -1s
    M = -np.ones((n, n), dtype=int)

    #index arrays of the board
    ind = np.indices((n, n))

    #creating the chessboard pattern by raising the elements to the power of the sum of their indeces
    M = np.power(M, ind[0] + ind[1])

    return M

def main():
    print(chessboard(3))

if __name__ == "__main__":
    main()