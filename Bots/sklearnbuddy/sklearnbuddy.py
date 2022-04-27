import random
from reconchess import *
from utils.boardtofen import *

# Next steps
# 1. get bot to understand/print the board as a fen
# 2. build a database where input variables are the characters that compose a fen and output variables are a) moves made by good bots or b) moves recommended by stockfish for the true match
# 3. Note that the one hot encoding will cover (6 pieces (ignore the blanks) * 2 colours * 64 squares = 768 columns!


class RandomBot(Player):

    def __init__(self):
        self.board = None
        self.color = None
        self.my_piece_captured_square = None

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.board = board
        self.color = color

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        self.my_piece_captured_square = capture_square
        if captured_my_piece:
            self.board.remove_piece_at(capture_square)

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        boardtofen(self.board)
        return random.choice(sense_actions)

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        for square, piece in sense_result:
            self.board.set_piece_at(square, piece)

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        return random.choice(move_actions + [None])

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        if taken_move is not None:
            self.board.push(taken_move)       

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass
