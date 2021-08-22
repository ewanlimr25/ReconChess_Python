import random
from reconchess import *
from Common_Util import *
from KillEm import *

## This file is to keep track of out understanding of what each function definition will entail and
## What we can do inside this function and what we should or can/will initialize inside of it.
## Just to keep track of our learning process on ReconChess.

class LearningBot(Player):

    ## handle_game_start This function takes in the player colour as the color variable in chess.WHITE or chess.BLACK
    ## board initilize the chess board as chess.board on your color and opponent_name is the name of your opponent.
    ## could handle initialization of the chess board based on color. Keep track of our pieces and where it is.


    def __init__(self):
        ## set the board as global to understand board state, can be used in choose_sense, choose_move
        self.myBoard = None

        ## set the color for our player
        self.color = None

        ## set the place where you piece was captured.
        self.my_piece_captured_square = None

        ## set a global for turn count and calculate possible moves.    
        self.myTurn = 0

        ## set to remember where my pieces are. This is a Dictionary that contains key:value where is chess.Piece : chess.Square
        self.fullBoard = None
        self.myPieces = None
        self.enemyKing = None
        self.myLostPieces = None
        self.enemyPieces = None


    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        ## set your global board
        self.myBoard = board
        self.color = color

        ## need to write in Util.py to include a helper function to set myPieces in a dictionary.
        self.fullBoard = chess.BaseBoard
        self.myPieces = CommonUtility.generatePieces(self.color)
        self.enemyPieces = CommonUtility.generatePieces(not self.color)
        self.myLostPieces = []
        

    ## handle_opponent_move_result takes in 2 parameters captured_my_piece and capture_square
    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        if captured_my_piece:
            self.my_piece_captured_square = capture_square
            removedPiece = self.myBoard.remove_piece_at(capture_square)
            self.myPieces.pop(removedPiece)
            

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:

            if self.myTurn < 6  and len(self.myLostPieces) == 0:

                if self.color is chess.WHITE:
                    return chess.F5
                else:
                    return chess.C4

            else:
                sense_location = KillEm.TargetLockOn(self.enemyPieces, self.myPieces, self.fullBoard)
                return sense_location

        
    ## think about how to keep track of unique Knights and Rooks on the sides of the board.
    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        ## will modify the pieces on the board for opponents.
        for move in sense_result:
            if move[1] is not None:
                self.fullBoard.set_piece_at(move[0],move[1])
                if move[1] is chess.KING and move[1].color is not self.color:
                    self.enemyKing = move[0]


    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        ## increase move by 1
        self.myTurn+=1

        return random.choice(move_actions + [None])

    ## think about how to keep track of unique Knights and Rooks on the sides of the board.
    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):

        if requested_move is taken_move:

            if captured_opponent_piece:
                ## look through enemy pieces
                for piece, square in self.enemyPieces.items():
                    if square is capture_square:
                        self.enemyPieces[piece].remove(square)
            
            self.myBoard.push(taken_move)

        else: ## some other random stuff is in the way lmfao.
            for piece, square in self.enemyPieces.items():
                    if square is capture_square:
                        self.enemyPieces[piece].remove(square)
            
            self.myBoard.push(taken_move)

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass