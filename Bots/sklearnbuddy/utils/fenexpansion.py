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
    return board_data


def parseJsonFile(file):
    return json.load(file)


def whiteWins(winningColor):
    return chess.WHITE == winningColor


def getFensBeforeMove(fen, color):
    if color == chess.WHITE:
        return fen["true"]
    else:
        return fen["false"]


#

# game_list = getGames()


# def getGames():
#    game_list = []
#    for root, dirs, files in os.walk("../../Games", topdown=False):
#       for name in files:
#          game_list.append(name)
#    return(game_list)
#
# game_list = getGames()
# print(game_list)


for root, dirs, files in os.walk("../../Games", topdown=False):
    fens_before_white_moves = []
    fens_before_black_moves = []
    white_moves = []
    black_moves = []
    winner = []
    for name in files:
        with open(os.path.join(root, name)) as json_file:
            data = json.load(json_file)
            fens_before_white_moves.append(
                getFensBeforeMove(data["fens_before_move"], chess.WHITE)
            )
            fens_before_black_moves.append(
                getFensBeforeMove(data["fens_before_move"], chess.BLACK)
            )
            white_moves.append(getFensBeforeMove(data["requested_moves"], chess.WHITE))
            black_moves.append(getFensBeforeMove(data["requested_moves"], chess.BLACK))
            winner.append(data["winner_color"])


# print(fens_before_black_moves[0][0])
# print(fens_before_white_moves[0][1])
# print(black_moves[0][0])
# print(winner[0])

# print(len(winner))
# print(len(black_moves))


fen1 = fenexpansion(fens_before_black_moves[0][0])

# white_won = pd.Series(1 if winner[0] else 0)
# blacks_move = pd.Series(black_moves[0][0]["value"])
# whites_turn = pd.Series(0).rename('whites_turn')
# fen1_with_winner = pd.concat((fen1, white_won.rename('white_won')), axis=1)
# fen1_with_winner_and_move = pd.concat((fen1_with_winner, blacks_move.rename('requested_move')), axis=1)
# fen1_full = pd.concat((fen1_with_winner_and_move, whites_turn), axis=1)
# print(fen1_full)

# Iterate through all of black's moves in game 0

full_df = pd.DataFrame()

for j in range(50):
    print(j)
    for i in range(len(black_moves[j])):
        white_won = pd.Series(1 if winner[j] else 0).rename("white_won")
        blacks_move = pd.Series(
            "skip" if black_moves[j][i] == None else black_moves[j][i]["value"]
        ).rename("requested_move")
        whites_turn = pd.Series(0).rename("whites_turn")
        current_fen = pd.concat(
            (fenexpansion(fens_before_black_moves[j][i]), white_won), axis=1
        )
        current_fen = pd.concat((current_fen, blacks_move), axis=1)
        current_fen = pd.concat((current_fen, whites_turn), axis=1)
        if i == 0 and j == 0:
            full_df = pd.DataFrame(columns=list(current_fen))
        full_df = pd.concat((full_df, current_fen), axis=0)

for j in range(50):
    for i in range(len(white_moves[j])):
        white_won = pd.Series(1 if winner[j] else 0).rename("white_won")
        whites_move = pd.Series(
            "skip" if white_moves[j][i] == None else white_moves[j][i]["value"]
        ).rename("requested_move")
        whites_turn = pd.Series(1).rename("whites_turn")
        current_fen = pd.concat(
            (fenexpansion(fens_before_white_moves[j][i]), white_won), axis=1
        )
        current_fen = pd.concat((current_fen, whites_move), axis=1)
        current_fen = pd.concat((current_fen, whites_turn), axis=1)
        full_df = pd.concat((full_df, current_fen), axis=0)


print(full_df)

full_df.to_csv("first_50_games.csv")


# board_data.loc[len(board_data)] = 0

# fen2 = fenexpansion(fens_before_black_moves[0][1])

# fen3 = pd.concat([fen1, fen2])
# print(fen3)

# print(fen3.to_csv("fen3.csv"))

board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"
test_board = fenexpansion(board)


# 1. Fens before move (DONE)
# 2. The move that was requested
# 3. Who won

# 1 row will be: [ the state of the board (fen) ] [ the move played following that fen ] [ if that move was made by a winner or loser (target variable!)]

# 1. [white_fen[0]] [white_requested_move[0]] [1 if white is winner, 0 if black is winner]
#    [...]
#    [blacl_fen[0]] [ ........................[1 if black is winner, 0 if white is winner]
