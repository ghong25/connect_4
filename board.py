import numpy as np


class Board:
    """
    By default, create a new game from an empty board, but potentially create game from an existing board position
    """
    def __init__(self, board_position=None, num_rows=6, num_cols=7):
        # initialize a new board if default value
        if board_position is None:
            self.board_state = np.zeros((num_rows, num_cols))
        # otherwise, create a new game on the basis of the existing board position
        else:
            self.board_state = board_position

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.player1 = 1
        self.player2 = 2

    # check to see if the game has been won
    def game_won(self, player):
        """
        take in player piece and check horizontal, vertical, pos diagonal, neg diagonal for 4 in a row. Return boolean
        indicating whether game is over
        """
        # Check horizontal locations for win
        for c in range(self.num_cols - 3):
            for r in range(self.num_rows):
                if self.board_state[r][c] == player and self.board_state[r][c + 1] == player and self.board_state[r][c + 2] \
                        == player and self.board_state[r][c + 3] == player:
                    return True

        # Check vertical locations for win
        for c in range(self.num_cols):
            for r in range(self.num_rows - 3):
                if self.board_state[r][c] == player and self.board_state[r + 1][c] == player and self.board_state[r + 2][c] \
                        == player and self.board_state[r + 3][c] == player:
                    return True

        # Check positively sloped diagonals
        for c in range(self.num_cols - 3):
            for r in range(self.num_rows - 3):
                if self.board_state[r][c] == player and self.board_state[r + 1][c + 1] == player and self.board_state[r + 2][c + 2] \
                        == player and self.board_state[r + 3][c + 3] == player:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.num_cols - 3):
            for r in range(3, self.num_rows):
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

    def is_valid_location(self, column):
        return self.board_state[0][column] == 0

    def get_valid_columns(self):
        """
        Return columns that are valid moves by checking the very top row for each column to see if it's empty
        """
        index = 0
        valid_col_index = []
        # check the top role to see if it's empty
        for col in self.board_state[0]:
            if col == 0:
                valid_col_index.append(index)
            index += 1
        return valid_col_index

    # return bool to see if the game has ended, either in a win or a tie
    def game_over(self):
        return self.game_won(self.player1) or self.game_won(self.player2) or len(self.get_valid_columns(self)) == 0

    # print current board
    def print_board(self):
        print(self.board_state)
