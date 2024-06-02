"""
Tic Tac Toe Player
"""

import math
import copy

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

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_counter += 1
            if cell == O:
                o_counter += 1
    if x_counter == o_counter:
        return X 
    else:
        return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_available = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_available.add((i, j))
    return actions_available
   
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception ('Invalid action')

    i, j = action
    new_bored = copy.deepcopy(board)
    new_bored[i][j] = player(new_bored)
    return new_bored
    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X  and board[0][1] == X and board[0][2] == X :
        return X 
    
    if board[1][0] == X  and board[1][1] == X and board[1][2] == X :
        return X 
    
    if board[2][0] == X  and board[2][1] == X and board[2][2] == X :
        return X 
    
    if board[0][0] == X  and board[1][0] == X and board[2][0] == X :
        return X 
    
    if board[0][1] == X  and board[1][1] == X and board[2][1] == X :
        return X 
    
    if board[0][2] == X  and board[1][2] == X and board[2][2] == X :
        return X 
    
    if board[0][0] == X  and board[1][1] == X and board[2][2] == X :
        return X 
    
    if board[0][2] == X  and board[1][1] == X and board[2][0] == X :
        return X 
    
    ############################################

    if board[0][0] == 'O' and board[0][1] == 'O'and board[0][2] == 'O':
        return 'O'
    
    if board[1][0] == 'O' and board[1][1] == 'O'and board[1][2] == 'O':
        return 'O'
    
    if board[2][0] == 'O' and board[2][1] == 'O'and board[2][2] == 'O':
        return 'O'
    
    if board[0][0] == 'O' and board[1][0] == 'O'and board[2][0] == 'O':
        return 'O'
    
    if board[0][1] == 'O' and board[1][1] == 'O'and board[2][1] == 'O':
        return 'O'
    
    if board[0][2] == 'O' and board[1][2] == 'O'and board[2][2] == 'O':
        return 'O'
    
    if board[0][0] == 'O' and board[1][1] == 'O'and board[2][2] == 'O':
        return 'O'
    
    if board[0][2] == 'O' and board[1][1] == 'O'and board[2][0] == 'O':
        return 'O'

    else:
        return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_counter = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_counter += 1
    if winner(board=board) == None and empty_counter > 1:
        return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board=board) == True and winner(board=board) == X :
        return 1
    if terminal(board=board) == True and winner(board=board) == 'O':
        return -1
    else:
        return 0

def Max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, Min_value(result(board, action)))
    return v

def Min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, Max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    elif player(board=board) == X :
        actions_played = []
        for action in actions(board):
            actions_played.append([Min_value(result(board,action)), action])
        return sorted(actions_played, key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board=board) == 'O':
        actions_played = []
        for action in actions(board):
            actions_played.append([Max_value(result(board=board, action=action)), action])
        return sorted(actions_played, key=lambda x: x[0])[0][1]
            




