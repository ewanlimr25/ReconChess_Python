import pandas as pd

# def fenexpansion(board):
#    print(board.fen())

def fenexpansion(board):
    split_fen_full = board.split()
    split_fen_board = split_fen_full[0].split("/")
    for row in split_fen_board:
        print(row)

board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"

print(fenexpansion(board))
