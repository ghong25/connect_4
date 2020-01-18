from board import Board
import math
import random

PLAYER1_PIECE = 1
AI_PIECE = 2

NUM_ROWS = 6
NUM_COLS = 7

WINDOW_LENGTH = 4


def evaluate_window(window, piece):
    """
    :param window: list representing a slice or subsection of the board
    :param piece: int for current player piece
    :return: int for evaluated score inside the window
    """
    score = 0
    opp_piece = PLAYER1_PIECE
    if piece == PLAYER1_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score


# function to evaluate current board position
def score_position(board, piece):
    """
    :param board: list of lists representing the current board state
    :param piece: int for the current player piece
    :return: int for the evaluated score
    """
    score = 0
    #  score center column
    center_array = [int(i) for i in list(board[:, NUM_COLS // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # horizontal
    for r in range(NUM_ROWS):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(NUM_COLS - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # vertical
    for c in range(NUM_COLS):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(NUM_ROWS - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # pos sloped diagonal
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # neg sloped diagonal
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def is_terminal_node(game):
    """
    :param game: game object
    :return: boolean representing whether the board state of game object represents a terminal node
    """
    return game.game_won(PLAYER1_PIECE) or game.game_won(AI_PIECE) or len(game.get_valid_columns()) == 0

# minimax algo with alpha-beta pruning for AI
def minimax(game, depth, alpha, beta, max_player):
    """
    :param game: take in  game object
    :param depth: depth of the traversal
    :param alpha: value for minimum score that the maximizing player is assured of
    :param beta: value for maximum score that the minimizing player is assured of
    :param max_player: boolean for whether the AI is the maximizing player
    :return: tuple that contains column and minimax score
    """
    # get the index positions of the remaining valid columns in which to make a move
    valid_col = game.get_valid_columns()
    # if you've reached a terminal node in the tree
    game_over = is_terminal_node(game)
    column = 0


    if depth == 0 or game_over:
        if game_over:
            if game.game_won(AI_PIECE):
                return None, 10000000000  # column and score
            elif game.game_won(PLAYER1_PIECE):
                return None, -10000000000
            else:  # game over, no valid moves
                return None, 0
        else:   # depth is zero
            return None, score_position(game.board_state, AI_PIECE)

    if max_player:
        value = -math.inf
        for col in valid_col:

            ### potentially setting the "new" board copy to the same obj in memory of the original, modifying original

            # create a new board object by passing in the current board state

            b_copy = Board(board_position=game.board_state.copy())
            b_copy.move(AI_PIECE, col)

            # recursively call minimax function
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # minimizing player
        value = math.inf
        column = random.choice(valid_col)
        for col in valid_col:
            b_copy = Board(board_position=game.board_state.copy())
            b_copy.move(PLAYER1_PIECE, col)
            # recursively call minimax function
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

