from reconchess import *
import random

# See https://lichess.org/study/9uARFiGm

class move_tree():
    def choose_move(self, color, turn, board, in_position, move_actions):
        WHITE_SYSTEM = [chess.Move.from_uci('g1f3'), # Nf3
            chess.Move.from_uci('g2g3'), # g3
            chess.Move.from_uci('f1g2'), # Bg2
            chess.Move.from_uci('e1g1'), # O-O
            chess.Move.from_uci('d2d3'), # d3
            chess.Move.from_uci('b1d2'), # Nbd2
            chess.Move.from_uci('f1e1'), # Re1
            chess.Move.from_uci('e2e4'), # e4
            chess.Move.from_uci('d1e2')] # Qe2

        BLACK_SYSTEM = [chess.Move.from_uci('g8f6'), # Nf6
            chess.Move.from_uci('g7g6'), # g6
            chess.Move.from_uci('f8g7'), # Bg7
            chess.Move.from_uci('e8g8'), # O-O
            chess.Move.from_uci('d7d6'), # d6
            chess.Move.from_uci('b8d7'), # Nbd7
            chess.Move.from_uci('f8e8'), # Re8
            chess.Move.from_uci('e7e5'), # e5
            chess.Move.from_uci('d8e7')] # Qe7
        
        my_system = WHITE_SYSTEM
        side = "white"

        if chess.BLACK:
            my_system = BLACK_SYSTEM
            side = "black"

        move = random.choice(move_actions + [None])
        
        if turn < len(my_system) and not in_position:
            if my_system[turn] in move_actions:
                move = my_system[turn]
                print("I'm {}. It's turn# {} and here's my move {}".format(side, turn, move))
                return move
        else:
            print("All out of theory moves - randomly playing {} now.".format(move))            
        return move