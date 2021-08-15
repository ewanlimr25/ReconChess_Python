from reconchess import *

## The purpose of this file is to establit a common functionality to be used to calculate movesets, weights, etc.
## This is a work in process for common functions. Specific calcualtion files will be separate from this one.

class CommonUtility:


    def generateBoard(self) -> chess.BaseBoard:
        return chess.BaseBoard


    def generatePieces(self, color):
        pieces = dict()
        if color == chess.WHITE:
            pieces["Rook"] = [chess.A1, chess.H1]
            pieces["Knight"] = [chess.B1, chess.G1]
            pieces["Bishop"] = [chess.C1, chess.F1]
            pieces["Queen"] = [chess.D1]
            pieces["King"] = [chess.E1]
            pieces["Pawn"] = [chess.A2, chess.B2,chess.C2,chess.D2,chess.E2,chess.F2,chess.G2,chess.H2]
        else:
            pieces["Rook"] = [chess.A8, chess.H8]
            pieces["Knight"] = [chess.B8, chess.G8]
            pieces["Bishop"] = [chess.C8, chess.F8]
            pieces["Queen"] = [chess.D8]
            pieces["King"] = [chess.E8]
            pieces["Pawn"] = [chess.A7, chess.B7,chess.C7,chess.D7,chess.E7,chess.F7,chess.G7,chess.H7]
        return pieces
    

