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

    # Remove the slashes (chess board rank separators) from the string
    pieces = pieces.replace("/","")
    expanded_board = ''
    
    # Iterate through pieces and replace blank numbers with the appropriate
    # number of '@'s. 
    for row in pieces:
        for character in row:
            if character.isdigit():
                expanded_board += int(character)*'@'
            else:
                expanded_board += character

    # Initialize blankboard with all 832 columns
    # Each column is a unique piece-square combination (e.g., a1Q is a column
    # with the value of '1' when there is a white queen on a1 and '0'
    # otherwise.
    board_data = blankboard()
    
    # List of all the column names in the main 832 column dataframe
    board_cols = list(board_data)

    # add a row of all zeros to the board
    board_data.loc[len(board_data)] = 0

    # determine which position on the board (e.g., a4) each piece belongs to
    # then flip that piece from a 0 to a 1
    for i in range(len(expanded_board)): 
        piece = expanded_board[i]
        rank = i // 8 + 1
        file = "abcdefgh"[i % 8]
        present_piece = file + str(rank) + piece
        board_data.loc[len(board_data)-1, present_piece] = 1
    
    print(board_data)
    board_data.to_csv("board_data.csv")
    
    board_data.iloc[0, 1] = 1
    a = "a1P"
    board_data.loc[0, a] = 1


board = "r1b1kbnr/ppp1p1pp/n7/3P1P1Q/3PP3/1BN2P2/PP2N1PP/R1BQK2R b KQkq - 0 5"

fenexpansion(board)
