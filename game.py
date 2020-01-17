import numpy as np
import math
import random

PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 2

PLAYER1 = 0
AI = 1

NUM_ROWS = 6
NUM_COLS = 7


class Game:
    def __init__(self):
        # rows, columns
        self.board_state = np.zeros((NUM_ROWS, NUM_COLS))

    # check to see if the game has been won
    def game_won(self, player):
        """
        take in player piece and check horizontal, vertical, pos diagonal, neg diagonal for 4 in a row. Return boolean
        indicating whether game is over
        """
        # Check horizontal locations for win
        for c in range(NUM_COLS - 3):
            for r in range(NUM_ROWS):
                if self.board_state[r][c] == player and self.board_state[r][c + 1] == player and self.board_state[r][c + 2] \
                        == player and self.board_state[r][c + 3] == player:
                    return True

        # Check vertical locations for win
        for c in range(NUM_COLS):
            for r in range(NUM_ROWS - 3):
                if self.board_state[r][c] == player and self.board_state[r + 1][c] == player and self.board_state[r + 2][c] \
                        == player and self.board_state[r + 3][c] == player:
                    return True

        # Check positively sloped diagonals
        for c in range(NUM_COLS - 3):
            for r in range(NUM_ROWS - 3):
                if self.board_state[r][c] == player and self.board_state[r + 1][c + 1] == player and self.board_state[r + 2][c + 2] \
                        == player and self.board_state[r + 3][c + 3] == player:
                    return True

        # Check negatively sloped diagonals
        for c in range(NUM_COLS - 3):
            for r in range(3, NUM_ROWS):
                if self.board_state[r][c] == player and self.board_state[r - 1][c + 1] == player and self.board_state[r - 2][c + 2] \
                        == player and self.board_state[r - 3][c + 3] == player:
                    return True

    def move(self, player, column):
        """
        Pass in player string and column number and place the player piece in that column, modifying the board
        """
        # iterate across the rows from the last one and place the piece in the first unoccupied row in that column
        n = 5
        piece_set = False
        while n >= 0:
            # continue if the spot is occupied
            if self.board_state[n][column] != 0:
                n -= 1
                continue
            # break out of loop if the column is empty for that row
            else:
                self.board_state[n][column] = player
                piece_set = True
                return n
        if not piece_set:
            next_move = input("Invalid Move: Please Make Another Selection: ")
            self.move(self, player, next_move - 1)

    # return bool to see if the game has ended, either in a win or a tie
    def game_over(self):
        return self.game_won(PLAYER1_PIECE) or self.game_won(AI_PIECE) or len(get_valid_columns(self.board_state)) == 0

    # print current board
    def print_board(self):
        print(self.board_state)


# Minimax and helper functions


# helper function for minimax
def get_valid_columns(board):
    """
    Return columns that are valid moves by checking the very top row for each column to see if it's empty
    """
    index = 0
    valid_col_index = []
    # check the top role to see if it's empty
    for col in board[0]:
        if col == 0:
            valid_col_index.append(index)
        index += 1
    return valid_col_index


# helper function for minimax, take in a game object and see if node is an end condition for the game
def is_terminal_node(game):
    return game.game_won(PLAYER1_PIECE) or game.game_won(AI_PIECE) or len(get_valid_columns(game.board_state)) == 0

# function to evaluate board positions
    #def

# minimax algo with alpha-beta pruning for AI
def minimax(game, depth, alpha, beta, max_player):
    """
    :param game: take in  game object
    :param depth: depth of the traversal
    :param alpha: value for
    :param beta: value for
    :param max_player: boolean for whether the AI is the maximizing player
    :return: tuple that contains column and score
    """
    # get the index positions of the remaining valid columns in which to make a move
    valid_col = get_valid_columns(game.board_state)
    # if you've reached a terminal node in the tree

    game_over = is_terminal_node(game)

    # maybe only need to define once
    column = 0

    if game_over:
        if game.game_won(AI_PIECE):
            return None, 10000000000  # column and score
        elif game.game_won(PLAYER1_PIECE):
            return None, -10000000000
        else:  # game over, no valid moves
            return None, 0

    if max_player:
        value = -math.inf
        #column = random.choice(valid_col)
        for col in valid_col:
            #row = get_next_open_row(board, col)
            g_copy = Game()
            g_copy.move(AI_PIECE, col)
            #drop_piece(b_copy, row, col, AI_PIECE)

            # recursively call minimax function
            new_score = minimax(g_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # minimizing player
        value = math.inf
        #column = random.choice(valid_col)
        for col in valid_col:
            #row = get_next_open_row(board, col)
            g_copy = Game()
            #drop_piece(b_copy, row, col, PLAYER_PIECE)
            g_copy.move(PLAYER1_PIECE, col)
            # recursively call minimax function
            new_score = minimax(g_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def main():
    # single or 2-player mode
    mode = input("2-player mode?  (Y/N): ")
    if mode.lower() == 'y':
        game = Game()
        while True:
            game.print_board()
            p1_move = input("Player 1, enter the column for your move: ")
            game.move(PLAYER1_PIECE, int(p1_move) - 1)
            if game.game_won(PLAYER1_PIECE):
                game.print_board()
                print("Game Over: Player 1 Wins")
                break
            game.print_board()
            print("-" * 45)
            p2_move = input("Player 2, Enter the column for your move: ")
            game.move(PLAYER2_PIECE, int(p2_move) - 1)
            if game.game_won(PLAYER2_PIECE):
                game.print_board()
                print("Game Over: Player 2 Wins")
                break
            print("-" * 45)
    # playing AI
    else:
        game = Game()
        while True:
            game.print_board()
            turn = 0
            if turn == PLAYER1:
                p1_move = input("Player 1, enter the column for your move: ")
                game.move(PLAYER1_PIECE, int(p1_move) - 1)
                if game.game_won(PLAYER1_PIECE):
                    game.print_board()
                    print("Game Over: You Win!")
                    break
                game.print_board()
                print("-" * 45)
                turn += 1
                turn = turn % 2
            if turn == AI:
                col, minimax_score = minimax(game, 5, -math.inf, math.inf, True)
                game.move(AI_PIECE, col)
                if game.game_won(AI_PIECE):
                    game.print_board()
                    print("Game Over: You lost.")
                    break
                game.print_board()
                print("-" * 45)
                turn += 1
                turn = turn % 2


main()
