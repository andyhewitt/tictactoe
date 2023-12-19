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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    # return [[O, O, O],
    #         [O, X,O],
    #         [X, O, X]]


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
    return X if (o_num == x_num) and (init is True) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    move = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                move.add((i, j))

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

    # Check the rows
    for row in board:
        if row[0] == row[1] == row[1] and row is not None:
            return row[0]
    # Check the columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    not_full_cell = True
    for rows in board:
        not_full_cell = not_full_cell and all(
            stone is not None for stone in rows)
    return not_full_cell


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_value = 0
    if winner(board) == X:
        win_value = 1
    if winner(board) == O:
        win_value = -1
    return win_value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


print(
    utility(initial_state())
)
