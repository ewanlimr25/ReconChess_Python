import pandas as pd
import chess
import os
import json


# The purpose of this function is to convert a FEN string into a row of data
# that can be fed into a regression model.
# (https://en.wikipedia.org/wiki/Dummy_variable_(statistics))


"""
6 fields:
    1. piece placement
    2. active color
    3. castling
    4. en passant target square
    5. halfmove clock
    6. fullmove number
"""

# Initialize a blank board that can capture any FEN in dummy variable form
def blankboard():
    board_coords = []

    # 1. pieces
    for number in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            for piecetype in [
                "P",
                "N",
                "B",
                "R",
                "Q",
                "K",
                "p",
                "n",
                "b",
                "r",
                "q",
                "k",
                "@",
            ]:
                board_coords.append(letter + number + piecetype)

    # 2. active colour
    # board_coords.append("active_colour")

    # # 3. castling
    # board_coords.append("K_castle_rights") # white kingside castle
    # board_coords.append("Q_castle_rights") # white queenside castle
    # board_coords.append("k_castle_rights") # black kingside castle
    # board_coords.append("q_castle_rights") # black queenside castle

    # # 4. en passant target square
    # # Not including this for now

    # # 5. halfmove clock - denotes how many moves it has been since the last capture or pawn advance
    # # This may be kind of meaningless for reconchess
    # board_coords.append("halfmove_clock")

    # # 6. fullmove number
    # board_coords.append("fullmove_number")

    board_df = pd.DataFrame(columns=board_coords)
    return board_df


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

    #   1. HANDLE PIECE INFORMATION ===========================================
    # Remove the slashes (chess board rank separators) from the string
    pieces = pieces.replace("/", "")
    expanded_board = ""

    # Replace blank squares with the appropriate number of '@'s.
    for row in pieces:
        for character in row:
            if character.isdigit():
                expanded_board += int(character) * "@"
            else:
                expanded_board += character

    # Initialize blankboard with all 832 columns
    board_data = blankboard()

    # List of all the column names in the main 832 column dataframe
    board_cols = list(board_data)

    # add a row of all zeros to the board
    board_data.loc[len(board_data)] = 0

    # If a piece is on a square, assign a '1' to the appropriate column
    for i in range(len(expanded_board)):
        piece = expanded_board[i]
        rank = i // 8 + 1
        file = "abcdefgh"[i % 8]
        present_piece = file + str(rank) + piece
        board_data.loc[len(board_data) - 1, present_piece] = 1

    # 3. ACTIVE COLOR
    # if active_colour == 'b':
    #    print("dog")
    # elif active_colour == 'w':
    #    print("cat")
    # else:
    #    raise ValueError('active_colour must be b or w, not ' + str(active_colour))

    board_data.to_csv("board_data.csv")

    return board_data


def getGames():
    return os.walk("../../Games")


def parseJsonFile(file):
    return json.load(file)


def whiteWins(winningColor):
    return chess.WHITE == winningColor


def getFensBeforeMove(fen, color):
    if color == chess.WHITE:
        return fen["true"]
    else:
        return fen["false"]


board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"

test_board = fenexpansion(board)

print(test_board)
