from board import Board
from ai import minimax
import math

PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 2

PLAYER1 = 0
AI = 1

NUM_ROWS = 6
NUM_COLS = 7


def main():
    # single or 2-player mode
    mode = input("2-player mode?  (Y/N): ")
    if mode.lower() == 'y':
        board = Board()
        while True:
            board.print_board()
            p1_move = int(input("Player 1, enter the column for your move: "))
            board.move(PLAYER1_PIECE, p1_move - 1)
            if board.game_won(PLAYER1_PIECE):
                board.print_board()
                print("Game Over: Player 1 Wins")
                break
            board.print_board()
            print("-" * 45)
            p2_move = int(input("Player 2, Enter the column for your move: "))
            board.move(PLAYER2_PIECE, p2_move - 1)
            if board.game_won(PLAYER2_PIECE):
                board.print_board()
                print("Game Over: Player 2 Wins")
                break
            print("-" * 45)
    # playing AI
    else:
        game_over = False
        board = Board()
        while not game_over:
            board.print_board()
            turn = 0
            if turn == PLAYER1:
                p1_move = int(input("Player 1, enter the column for your move: "))
                board.move(PLAYER1_PIECE, p1_move - 1)
                if board.game_won(PLAYER1_PIECE):
                    board.print_board()
                    print("Game Over: You Win!")
                    game_over = True
                board.print_board()
                print("-" * 45)
                turn += 1
                turn = turn % 2
            if turn == AI and not game_over:
                col = minimax(board, 5, -math.inf, math.inf, True)[0]
                print(col, board.is_valid_location(col))
                if board.is_valid_location(col):
                    board.move(AI_PIECE, col)
                    if board.game_won(AI_PIECE):
                        board.print_board()
                        print("Game Over: You lost.")
                        game_over = True
                board.print_board()
                print("-" * 45)
                turn += 1
                turn = turn % 2


main()
