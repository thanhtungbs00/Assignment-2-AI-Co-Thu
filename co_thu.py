from main import Piece, Board
# ======================== Class Player =======================================


class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    # Student MUST implement this function
    # The return value should be a move that is denoted by:
        # piece: selected piece
        # (row, col): new position of selected piece
    def next_move(self, state):
        piece = Piece('Voi', (6, 7))
        new_pos = (7, 7)
        return piece, new_pos

