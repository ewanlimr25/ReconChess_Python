from reconchess import *
import chess
import os
import json

## The purpose of this file is to establit a common functionality to be used to calculate movesets, weights, etc.
## This is a work in process for common functions. Specific calcualtion files will be separate from this one.


class CommonUtility:
    def generateBoard(self) -> chess.BaseBoard:
        return chess.BaseBoard

    def generatePieces(self, color):
        pieces = dict()
        if color == chess.WHITE:
            pieces[chess.A1] = chess.Piece(chess.ROOK, color)
            pieces[chess.H1] = chess.Piece(chess.ROOK, color)
            pieces[chess.B1] = chess.Piece(chess.KNIGHT, color)
            pieces[chess.G1] = chess.Piece(chess.KNIGHT, color)
            pieces[chess.C1] = chess.Piece(chess.BISHOP, color)
            pieces[chess.F1] = chess.Piece(chess.BISHOP, color)
            pieces[chess.D1] = chess.Piece(chess.QUEEN, color)
            pieces[chess.E1] = chess.Piece(chess.KING, color)
            pieces[chess.A2] = chess.Piece(chess.PAWN, color)
            pieces[chess.B2] = chess.Piece(chess.PAWN, color)
            pieces[chess.C2] = chess.Piece(chess.PAWN, color)
            pieces[chess.D2] = chess.Piece(chess.PAWN, color)
            pieces[chess.E2] = chess.Piece(chess.PAWN, color)
            pieces[chess.F2] = chess.Piece(chess.PAWN, color)
            pieces[chess.G2] = chess.Piece(chess.PAWN, color)
            pieces[chess.H2] = chess.Piece(chess.PAWN, color)
        else:
            pieces[chess.A8] = chess.Piece(chess.ROOK, color)
            pieces[chess.H8] = chess.Piece(chess.ROOK, color)
            pieces[chess.B8] = chess.Piece(chess.KNIGHT, color)
            pieces[chess.G8] = chess.Piece(chess.KNIGHT, color)
            pieces[chess.C8] = chess.Piece(chess.BISHOP, color)
            pieces[chess.F8] = chess.Piece(chess.BISHOP, color)
            pieces[chess.D8] = chess.Piece(chess.QUEEN, color)
            pieces[chess.E8] = chess.Piece(chess.KING, color)
            pieces[chess.A7] = chess.Piece(chess.PAWN, color)
            pieces[chess.B7] = chess.Piece(chess.PAWN, color)
            pieces[chess.C7] = chess.Piece(chess.PAWN, color)
            pieces[chess.D7] = chess.Piece(chess.PAWN, color)
            pieces[chess.E7] = chess.Piece(chess.PAWN, color)
            pieces[chess.F7] = chess.Piece(chess.PAWN, color)
            pieces[chess.G7] = chess.Piece(chess.PAWN, color)
            pieces[chess.H7] = chess.Piece(chess.PAWN, color)
        return pieces

    def getGames(self):
        return os.walk("../Games")

    def parseJsonFile(self, file):
        return json.load(file)

    def whiteWins(self, winningColor):
        return chess.WHITE == winningColor

    def getFenAfterMove(self, fen, color):
        if color == chess.WHITE:
            return fen["true"]
        else:
            return fen["false"]
