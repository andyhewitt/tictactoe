"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    init = True
    for rows in board:
        init = init and all(stone is None for stone in rows)

    for rows in board:
        x_num = 0
        o_num = 0
        for stone in rows:
            if stone == X:
                x_num += 1
            elif stone == O:
                o_num += 1
    return X if (o_num == x_num) and (init == True) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    move = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == None:
                move.add((i,j))

    return move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Not a valid move")
    
    move_type = player(board)
    board[action[0]][action[1]] = move_type
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

print(result(initial_state(),(0,0)))