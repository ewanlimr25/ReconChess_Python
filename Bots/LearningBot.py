import random
from reconchess import *
from Common_Util import *
from KillEm import *

# This file is to keep track of out understanding of what each function definition will entail and
# What we can do inside this function and what we should or can/will initialize inside of it.
# Just to keep track of our learning process on ReconChess.


class LearningBot(Player):

    # handle_game_start This function takes in the player colour as the color variable in chess.WHITE or chess.BLACK
    # board initilize the chess board as chess.board on your color and opponent_name is the name of your opponent.
    # could handle initialization of the chess board based on color. Keep track of our pieces and where it is.

    def __init__(self):
        # set the board as global to understand board state, can be used in choose_sense, choose_move
        self.myBoard = None

        # set the color for our player
        self.color = None

        # set the place where you piece was captured.
        self.my_piece_captured_square = None

        # set a global for turn count and calculate possible moves.
        self.myTurn = 0

        # set to remember where my pieces are. This is a Dictionary that contains key:value where is chess.Piece : chess.Square
        self.myPieces = None
        self.enemyKing = None
        self.myLostPieces = None
        self.enemyPieces = None
        self.opponent_name = None
        self.unknownTakenEnemyPieces = None  # used in handle_move_result

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        # set your global board
        # need to look more into chess.Board class to understand its uses.
        self.myBoard = board
        self.color = color

        self.myPieces = CommonUtility.generatePieces(self.color)
        self.enemyPieces = CommonUtility.generatePieces(not self.color)
        self.myLostPieces = []
        self.unknownTakenEnemyPieces = []
        self.opponent_name = opponent_name

    # handle_opponent_move_result takes in 2 parameters captured_my_piece and capture_square

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        if captured_my_piece:
            self.my_piece_captured_square = capture_square
            removedPiece = self.myBoard.remove_piece_at(capture_square)
            if removedPiece is not None:
                self.myPieces.pop(capture_square)

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:

        if self.myTurn < 6 and len(self.myLostPieces) == 0:

            if self.color is chess.WHITE:
                return chess.F5
            else:
                return chess.C4

        else:
            sense_location = KillEm.TargetLockOn(
                self.enemyPieces, self.myPieces, self.myBoard)
            return sense_location

    # think about how to keep track of unique Knights and Rooks on the sides of the board.
    # reminder to push results to the board if found discrepencies in the board.

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        # will modify the pieces on the board for opponents.
        for square, piece in sense_result:
            # print("Handle_sense_result - Square:{}".format(square))
            # print("Handle_sense_result - Piece:{}".format(piece))
            if piece is not None:
                if self.myBoard.piece_at(square) is not piece:
                    ## think of a away to create the enemy move.
                    self.myBoard.push()

            self.board.set_piece_at(square, piece)

        #for move in sense_result:
        #    if move[1] is not None:
        #        self.myBoard.set_piece_at(move[0], move[1])
        #        if move[1] is chess.KING and move[1].color is not self.color:
        #            self.enemyKing = move[0]

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        # increase move by 1
        self.myTurn += 1

        return random.choice(move_actions + [None])

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):

        if captured_opponent_piece:

            takenPiece = self.myBoard.remove_piece_at(taken_move.to_square)

            if capture_square in self.enemyPieces and self.enemyPieces[capture_square] is takenPiece:
                # remove enemy pieces
                self.enemyPieces.pop(capture_square)

            else:
                # Sept 5, 2021, gotta handle unknown piece taken.
                self.unknownTakenEnemyPieces.append(taken_move.to_square)

        self.myBoard.push(taken_move)

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass
