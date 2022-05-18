import pandas as pd



# The purpose of this function is to convert a FEN string into a row of data
# that can be fed into a regression model.
# (https://en.wikipedia.org/wiki/Dummy_variable_(statistics))

def fenexpansion(board):
    # Split the FEN string into individual fields
    split_fen_full = board.split()

    # Assign each FEN field to a variable
    pieces = split_fen_full[0]
    active_colour = split_fen_full[1]
    castling = split_fen_full[2]
    en_passant = split_fen_full[3]
    halfmove_clock = split_fen_full[4]
    fullmove_number = split_fen_full[5]

    board_rows = pieces.split("/")

    for row in board_rows:
        for character in row:
            if


    return(board_rows)

board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"




"""
6 fields:
    1. piece placement
    2. active color
    3. castling
    4. en passant target square
    5. halfmove clock
    6. fullmove number
"""

print(fenexpansion(board))
