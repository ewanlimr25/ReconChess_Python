from reconchess import *
import random


class move_tree():
    def choose_move(self, color, turn, board, move_actions):
        WHITE_SYSTEM = [chess.Move.from_uci('g1f3'), 
            chess.Move.from_uci('g2g3'),
            chess.Move.from_uci('f1f2'),
            chess.Move.from_uci('e1g1')]
        BLACK_SYSTEM = [chess.Move.from_uci('g8f6'), 
            chess.Move.from_uci('g7g6'),
            chess.Move.from_uci('f8f7'),
            chess.Move.from_uci('e8g8')]
        move = random.choice(move_actions + [None])
        if color:
            my_system = WHITE_SYSTEM
            side = "white"
        else:
            my_system = BLACK_SYSTEM
            side = "black"
        if my_system[turn] in move_actions:
            move = my_system[turn]
        print("I'm {}. It's turn# {} and here's my move {}".format(side, turn, move))
        return move


class black_moves():
    def choose_move(self):
        print("I'm black and here's my move")
        return random.choice(move_actions + [None])
