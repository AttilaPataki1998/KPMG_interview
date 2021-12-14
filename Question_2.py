import numpy as np

def num_of_valid_cells(n, r_q, c_q, obstacles):
    """Calculates the number of squares a queen can attack"""

    #an nxn array of zeroes representing the chessboard
    board = np.zeros((n, n), dtype = int)
    
    #placing down the obstacles on the board. I assumed, that the queen can't have the same coordinates as any of the obstacles
    for obstacle in obstacles:
        board[obstacle[0] - 1][obstacle[1] - 1] = -1

    #the starting position of the queen
    r = r_q-1
    c = c_q-1

    #this section checks on which squares can the queen move by replacing the appropriate zeros with ones in the board
    #checking down
    for i in np.arange(1, r_q):
        if board[r - i][c] == -1:
            break
        else:
            board[r - i][c] = 1

    #checking up
    for i in np.arange(r_q, n):
        if board[i][c] == -1:
            break
        else:
            board[i][c] = 1

    #checking left
    for i in np.arange(1, c_q):
        if board[r][c - i] == -1:
            break
        else:
            board[r][c - i] = 1

    #checking right
    for i in np.arange(c_q, n):
        if board[r][i] == -1:
            break
        else:
            board[r][i] = 1

    #checking diagonally down, left
    for i in np.arange(1, np.minimum(r_q, c_q)):
        if board[r - i][c - i] == -1:
            break
        else:
            board[r- i][c - i] = 1
    
    #checking diagonally down, right
    for i in np.arange(1, np.minimum(r_q, n-c_q+1)):
        if board[r - i][c + i] == -1:
            break
        else:
            board[r - i][c + i] = 1

    #checking diagonally up, left
    for i in np.arange(1, np.minimum(n-r_q+1, c_q)):
        if board[r + i][c - i] == -1:
            break
        else:
            board[r + i][c - i] = 1

    #checking diagonally up, right
    for i in np.arange(1, np.minimum(n-r_q+1, n-c_q+1)):
        if board[r + i][c + i] == -1:
            break
        else:
            board[r + i][c + i] = 1

    #printing out the number of attackable cells
    print(np.count_nonzero(board == 1))

num_of_valid_cells(8, 4, 4, [np.array([3, 5])])