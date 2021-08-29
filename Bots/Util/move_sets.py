from reconchess import *
import random


class move_tree():
    def choose_move(self, move_actions):
        return random.choice(move_actions + [None])
            # WHITE_SYSTEM = [chess.Move.from_uci('g1f3'), 
            #     chess.Move.from_uci('g2g3'),
            #     chess.Move.from_uci('f1f2'),
            #     chess.Move.from_uci('e1g1')]

class black_moves():
    def choose_move(self):
        print("I'm black and here's my move")
        return random.choice(move_actions + [None])
            # BLACK_SYSTEM = [chess.Move.from_uci('g8f6'), 
            #     chess.Move.from_uci('g7g6'),
            #     chess.Move.from_uci('f8f7'),
            #     chess.Move.from_uci('e8g8')]