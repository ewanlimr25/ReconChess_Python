import pandas as pd


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

def blankboard():
    board_coords = []
    for number in ['1', '2', '3', '4', '5', '6', '7', '8']:
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            for piecetype in ['P', 'N', 'B', 'R', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k', '@']:
                board_coords.append(letter + number + piecetype)
    board_df = pd.DataFrame(columns = board_coords)
    return(board_df)

def miniboard(): # practice with a smaller board before implementing blankboard
    board_coords = []
    for number in ['1', '2', '3']:
        pass

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

    # Iterate through pieces and replace blank numbers with the appropriate
    # number of '@'s
    pieces = pieces.replace("/","")
    expanded_board = ''
    for row in pieces:
        for character in row:
            if character.isdigit():
                expanded_board += int(character)*'@'
            else:
                expanded_board += character

    # Initialize blankboard with all 832 columns
    board_data = blankboard()
    
    # List of all the column names in the main 832 column dataframe
    board_cols = list(board_data)

    for piece in expanded_board:
        print(piece)


    # board_data.loc[0] = list(expanded_board)
    # board_data = pd.get_dummies(board_data)
    
    return(board_cols)
#   return(expanded_board)

board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"

print(fenexpansion(board))
