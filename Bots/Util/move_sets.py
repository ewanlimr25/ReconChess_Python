from reconchess import *
import random

# See https://lichess.org/study/9uARFiGm

class move_tree():
    def choose_move(self, color, turn, board, theory_status, move_actions):
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
        
        # assign moveset based on colour
        my_system = WHITE_SYSTEM
        side = "white"
        if not color: # if the bot is playing black
            my_system = BLACK_SYSTEM
            side = "black"

        # Hard-coded situations to avoid. 
        # 1. A pawn is pushed 2 squares (threatents displacing the kingside night)
        if theory_status:
            if color: # if the bot is playing white
                if board.piece_at(chess.E5) is not None: 
                    if board.piece_at(chess.E5).symbol() == 'p':
                        print("Emergency type 1 - Pawn is threatening the f3 square. Will attempt to play d3.")
                        theory_status = False
                        move = chess.Move.from_uci('d2d3')
                        if move in move_actions:
                            return move, theory_status
                        else:
                            print("Unable to play d3. Playing random move.")
                            theory_status = False
                            return random.choice(move_actions + [None]), theory_status
            else: # if the bot is playing black
                if board.piece_at(chess.E4) is not None:
                    if board.piece_at(chess.E4).symbol() == 'P':
                        print("Emergency type 1 - Pawn is threatening the f6 square. Will attempt to play d6.")
                        theory_status = False
                        move = chess.Move.from_uci('d7d6')
                        if move in move_actions:
                            return move, theory_status
                        else:
                            print("Unable to play d3. Playing random move.")
                            theory_status = False
                            return random.choice(move_actions + [None]), theory_status

        
        # assign hard-coded move if possible.
        # if not possible, assign random move.
        # start with a random move
        move = random.choice(move_actions + [None])
        if turn < len(my_system) and theory_status:
            if my_system[turn] in move_actions:
                move = my_system[turn]
                print("I'm {}. It's turn #{} and here's my move {}".format(side, turn, move))
        else:
            theory_status = False
            print("All out of theory moves - randomly playing {} now.".format(move))            
        return move, theory_status