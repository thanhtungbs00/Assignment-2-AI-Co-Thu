from main import Piece, Board
# ======================== Class Player =======================================


class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return str(self.str)

    # Student MUST implement this function
    # The return value should be a move that is denoted by:
        # piece: selected piece
        # (row, col): new position of selected piece
    def next_move(self, state):
        piece = Piece('Voi', (7, 7))
        new_pos = (6, 7)
        return piece, new_pos

    def lstmove(self, piece):
        # some special case : 4 corner (1,1);(1,7)-(9,1);(9,7)
        if piece.position in [(1,1)]:
            return [(1,2), (2,1)]
        elif piece.position in [(1,7)]:
            return [(1,6), (2,7)]
        elif piece.position in [(9,1)]:
            return [(8,1), (9,2)]
        elif piece.position in [(9,7)]:
            return [(9,6), (8,7)]
        row = piece.position[0]
        col = piece.position[1]
        ani = piece.type    # name of animal 
        if ani in ['Voi', 'Soi', 'Cho', 'Chuot']:
            if row in [2,3,4,5,6,7,8] and col in [2,3,4,5,6]:
                return [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
            elif row == 1:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row+1, col)]
            elif row == 9:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row-1, col)]
            elif col == 1:
                return [(row, col+1),(row+1, col),(row-1, col)]
            elif col == 7:
                return [(row, col-1),(row+1, col),(row-1, col)]
        elif ani in ['SuTu', 'Ho', 'Bao', 'Meo']:
            if row == 1:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row+1, col)]
            elif row == 9:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row-1, col)]
            elif row in [2,8] and not (col in [1,7]):
                return [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
            elif col == 4 and row in [3,7]:
                return [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
            elif row in [2,3,7,8] and col == 1:
                return [(row+1, col),(row-1, col),(row, col+1)]
            elif row in [2,3,7,8] and col == 7: 
                return [(row+1, col),(row-1, col),(row, col-1)]
            # can jump through river
            if ani in ['SuTu', 'Ho', 'Bao']:
                if row in [4,5,6] and col == 1:
                    return [(row+1, col),(row-1, col),(row, col+3)]
                elif row in [4,5,6] and col == 7:
                    return [(row+1, col),(row-1, col),(row, col-3)]
                elif row in [4,5,6] and col == 4:
                    return [(row+1, col),(row-1, col),(row, col+3),(row, col-3)]
                if row == 3 and col in [2,3,5,6]:
                    if ani in ['SuTu', 'Ho']:
                        return [(row, col+1),(row, col-1),(row-1, col),(row+4,col)]
                    else:   # Bao
                        return [(row, col+1),(row, col-1),(row+1, col)]
            elif ani in ['Meo']:
                if row in [4,5,6]: # apply both col = 1 and 7 anh 4
                    return [(row+1, col),(row-1, col)]
                elif row == 3:
                    return [(row, col+1),(row, col-1),(row-1, col)]
                elif row == 7:
                    return [(row, col+1),(row, col-1),(row+1, col)]    
