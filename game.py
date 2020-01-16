import numpy as np
import math
import random

PLAYER1_PIECE = 1
PLAYER1 = 1
PLAYER2_PIECE = 2
AI_PIECE = 2
AI = 2

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

    # function to evaluate board positions
    #def

    # minimax algo with alpha-beta pruning for AI
    def minimax(self, depth, alpha, beta, maximizingPlayer):
        """
        #:param depth: depth of the traversal
        #:param alpha: value for
        #:param beta: value for
        #:param maximizingPlayer: boolean for whether the AI is the maximizing player
        #:return: tuple that contains column and score
        """
        # get the index positions of the remaining valid columns in which to make a move
        valid_col = self.get_valid_columns(self)
        # if you've reached a terminal node in the tree
        game_over = self.game_won(self)

        # maybe only need to define once
        column = 0

        if depth == 0 or game_over:
            if game_over:
                if self.game_won(self, AI_PIECE):
                    return None, 10000000000  # column and score
                elif self.game_won(self, PLAYER1_PIECE):
                    return None, -10000000000
                else:  # game over, no valid moves
                    return None, 0
            else:  # depth is zero
                #return None, self.score_position(board, AI_PIECE)
                return None, 0

        if maximizingPlayer:
            value = -math.inf
            #column = random.choice(valid_col)
            for col in valid_col:
                #row = get_next_open_row(board, col)
                b_copy = self.board.copy()
                self.move(self, AI_PIECE, col)
                #drop_piece(b_copy, row, col, AI_PIECE)

                # recursively call minimax function
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
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
                b_copy = self.board.copy()
                #drop_piece(b_copy, row, col, PLAYER_PIECE)
                self.move(self, PLAYER1_PIECE, col)
                # recursively call minimax function
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
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
        board = Board()
        while True:
            board.print_board()
            p1_move = input("Player 1, enter the column for your move: ")
            board.move(PLAYER1_PIECE, int(p1_move) - 1)
            if board.game_won(PLAYER1_PIECE):
                board.print_board()
                print("Game Over: Player 1 Wins")
                break
            board.print_board()
            print("-" * 45)
            p2_move = input("Player 2, Enter the column for your move: ")
            board.move(PLAYER2_PIECE, int(p2_move) - 1)
            if board.game_won(PLAYER2_PIECE):
                board.print_board()
                print("Game Over: Player 2 Wins")
                break
            print("-" * 45)
    else:
        board = Board()
        turn = 1
        if turn == PLAYER1:
            p1_move = input("Player 1, enter the column for your move: ")
            board.move(PLAYER1_PIECE, int(p1_move) - 1)


main()


    if turn == PLAYER:
        posx = event.pos[0]
        col = int(math.floor(posx / SQUARESIZE))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)

            if winning_move(board, PLAYER_PIECE):
                label = myfont.render("Player 1 wins!!", 1, RED)
                screen.blit(label, (40, 10))
                game_over = True

            turn += 1
            turn = turn % 2

            print_board(board)
            draw_board(board)

# Ask for Player 2 Input
if turn == AI and not game_over:
    col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, AI_PIECE)

        if winning_move(board, AI_PIECE):
            label = myfont.render("Player 2 wins!!", 1, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True

        print_board(board)
        draw_board(board)

    turn += 1
    turn = turn % 2