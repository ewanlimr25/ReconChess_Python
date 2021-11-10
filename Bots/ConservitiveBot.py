import chess.engine
import random
import os
from reconchess import *
import Util.move_sets as ut


STOCKFISH_ENV_VAR = '../stockfish/stockfish_13_win_x64_bmi2.exe'

## Will construct this bot to be conservative and play within own 4 spaces and establish defences.
class conservative_bot(Player):
    def __init__(self):
        ## set the board as global to understand board state, can be used in choose_sense, choose_move
        self.myBoard = None

        ## set the color for our player
        self.color = None

        ## set the place where you piece was captured.
        self.my_piece_captured_square = None

        ## set a global for turn count and calculate possible moves.    
        self.myTurn = -1

        ## set to remember where my pieces are. This is a Dictionary that contains key:value where is chess.Piece : chess.Square
        self.myPieces = None

        ## set to determine which set of opening moves will be used
        self.my_system = None

        ## set to keep track of how many moves of hard-coded theory have been made.
        ## starts at -1 as the value is incremented prior to choose_move returning the next theory move.
        self.opening_count = -1

        ## set to determine if the hard-coded theory stage is complete
        self.theory_status = True
       


    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.board = board
        self.color = color  # Boolean value where chess.WHITE = True and chess.BLACK = FALSE
      
    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        pass

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        if not self.theory_status:
            chosen_sense = random.choice(sense_actions)
        elif self.theory_status:
            if self.color == True:
                chosen_sense = chess.F5
            elif self.color == False:
                chosen_sense = chess.F4
        print("\n\nTURN NUMBER {}".format(self.myTurn + 1))
        print("Our 'theory' status is {}.\nI sensed square {}".format(self.theory_status, chosen_sense))
        return chosen_sense



    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        print("From my sense, I observed {}".format(sense_result))
        for square, piece in sense_result:
            self.board.set_piece_at(square, piece)


    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        self.myTurn += 1
        move_tree = ut.move_tree()
        move, self.theory_status = move_tree.choose_move(self.color, self.myTurn, self.board, self.theory_status, move_actions)
        return move

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        pass

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass
