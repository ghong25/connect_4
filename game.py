import numpy as np

PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 2

NUM_ROWS = 6
NUM_COLS = 7

class Board:
    def __init__(self):
        # rows, columns
        self.board = np.zeros((NUM_ROWS, NUM_COLS))
        # playable columns ?

    # check to see if the game has been won
    def game_won(self, player):
        """
        take in player piece and check horizontal, vertical, pos diagonal, neg diagonal for 4 in a row. Return boolean
        indicating whether game is over
        """
        # Check horizontal locations for win
        for c in range(NUM_COLS - 3):
            for r in range(NUM_ROWS):
                if self.board[r][c] == player and self.board[r][c + 1] == player and self.board[r][c + 2] == player and \
                        self.board[r][c + 3] == player:
                    return True

        # Check vertical locations for win
        for c in range(NUM_COLS):
            for r in range(NUM_ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c] == player and self.board[r + 2][c] == player and \
                        self.board[r + 3][c] == player:
                    return True

        # Check positively sloped diagonals
        for c in range(NUM_COLS - 3):
            for r in range(NUM_ROWS - 3):
                if self.board[r][c] == player and self.board[r + 1][c + 1] == player and self.board[r + 2][c + 2] == \
                        player and self.board[r + 3][c + 3] == player:
                    return True

        # Check negatively sloped diagonals
        for c in range(NUM_COLS - 3):
            for r in range(3, NUM_ROWS):
                if self.board[r][c] == player and self.board[r - 1][c + 1] == player and self.board[r - 2][c + 2] == \
                        player and self.board[r - 3][c + 3] == player:
                    return True

    def is_valid_move(self, col):
        # check to make sure that the move is in an empty space
        #if self.move()
        pass

    def move(self, player, column):
        """
        Pass in player string and column number and place the player piece in that column, modifying the board
        """
        # iterate across the rows from the last one and place the piece in the first unoccupied row in that column
        n = 5
        piece_set = False
        while n >= 0:
            # continue if the spot is occupied
            if self.board[n][column] != 0:
                n -= 1
                continue
            # break out of loop if the column is empty for that row
            else:
                self.board[n][column] = player
                piece_set = True
                return n
        if not piece_set:
            next_move = input("Invalid Move: Please Make Another Selection: ")
            self.move(self, player, next_move - 1)

    def get_valid_columns(self):
        """
        Return columns that are valid moves by checking the very top row for each column to see if it's empty
        """
        index = 0
        valid_col_index = []
        # check the top role to see if it's empty
        for col in self.board[0]:
            if col == 0:
                valid_col_index.append(index)
            index += 1
        return valid_col_index

    # print current board
    def print_board(self):
        print(self.board)

    # helper function for minimax, see if node is an end condition for the game
    def is_terminal_node(self):
        return self.game_won(self, PLAYER1_PIECE) or self.game_won(self, AI_PIECE) or len(self.get_valid_columns(self)) == 0

"""
    # minimax algo with alpha-beta pruning for AI
    def minimax(self, depth, alpha, beta, maximizingPlayer):
        """
        #:param depth: depth of the traversal
        #:param alpha: value for
        #:param beta: value for
        #:param maximizingPlayer: boolean for whether the AI is the maximizing player
        #:return:
"""
        # get the index positions of the remaining valid columns in which to make a move
        valid_col = self.get_valid_columns(self)
        # if you've reached a terminal node in the tree
        game_over = self.game_won(self)
        if depth == 0 or game_over:
            if game_over:
                if winning_move(board, AI_PIECE):
                    return None, 10000000000  # column and score
                elif winning_move(board, PLAYER_PIECE):
                    return None, -10000000000
                else:  # game over, no valid moves
                    return None, 0
            else:  # depth is zero
                return None, score_position(board, AI_PIECE)

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
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
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
"""


def main():
    # single or 2-player mode
    mode = input("2-player mode?  (Y/N): ")
    if mode.lower() == 'y':
        board = Board()
        while True:
            board.print_board()
            p1_move = input("Player 1, enter the column for your move: ")

            # catch invalid column errors
            col = board.move(1, int(p1_move) - 1)
            if board.game_over(PLAYER1_PIECE):
                board.print_board()
                print("Game Over: Player 1 Wins")
                break
            board.print_board()
            print("-" * 45)
            p2_move = input("Player 2, Enter the column for your move: ")
            col2 = board.move(2, int(p2_move) - 1)
            if board.game_over(PLAYER2_PIECE):
                board.print_board()
                print("Game Over: Player 2 Wins")
                break
            print("-" * 45)
    else:
        #board = Board()
        print("Done")


main()
