from main import Piece, Board
import copy, math
INF = math.inf
# ======================== Class Player =======================================

class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return str(self.str)
    
    def evaluatePosition(self, state):
        score_black = 0
        score_red = 0
        for x in state.list_red:
            score_red += self.getDevelopValue(x, "red")
            score_red += self.getMaterialValue(x)
        for x in state.list_black:
            score_black += self.getDevelopValue(x, "black")
            score_black += self.getMaterialValue(x) 
        if (self.str.lower() == "red"):
            return score_red - score_black
        else:
            return score_black - score_red

    def getValue(self, piece):
        animal = piece.type
        if (self.str.lower() == "red"):
            if piece.position == (9,3) or piece.position == (9,5) or piece.position == (8,4):
                return -1
        else:
            if piece.position == (2,4) or piece.position == (1,5) or piece.position == (1,3):
                return -1
        if animal.lower() == "chuot":
            return 1
        elif animal.lower() == "meo":
            return 2
        elif animal.lower() == "soi":
            return 3
        elif animal.lower() == "cho":
            return 4
        elif animal.lower() == "bao":
            return 5
        elif animal.lower() == "ho":
            return 6
        elif animal.lower() == "sutu":
            return 7
        elif animal.lower() == "voi":
            return 8
    
    def checkDefeat(self, piece, rival):
        a = self.getValue(piece)
        b = self.getValue(rival)
        if (a==1) and (b==8):
            return True
        elif (a >= b):
            return True
        else :
            return False

    def getMaterialValue(self, piece):
        animal = piece.type
        
        if animal.lower() == "chuot":
            return 500
        elif animal.lower() == "meo":
            return 200
        elif animal.lower() == "soi":
            return 300
        elif animal.lower() == "cho":
            return 400
        elif animal.lower() == "bao":
            return 500
        elif animal.lower() == "ho":
            return 800
        elif animal.lower() == "sutu":
            return 900
        elif animal.lower() == "voi":
            return 1000

    def getDevelopValue(self, piece, list_type):
        if (piece.type.lower() == "chuot"):
            lst_value = [[11, 13, 50, 99999, 50, 13, 13],
                         [11, 12, 13, 50   , 13, 13, 13],
                         [10, 11, 11, 13   , 13, 13, 13],
                         [8 , 9 , 9 , 11   , 12, 12, 13],
                         [8 , 9 , 9 , 11   , 12, 12, 12],
                         [8 , 9 , 9 , 10   , 12, 12, 11],
                         [8 , 8 , 8 , 9    , 10, 10, 10],
                         [8 , 8 , 8 , 9    , 9 , 9 ,  9],
                         [8 , 8 , 8 , 0    , 8 , 8 ,  8]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
            
        elif (piece.type.lower() == "meo"):
            lst_value = [[11, 15, 50, 99999, 50, 15, 11],
                         [11, 11, 15, 50   , 15, 11, 11],
                         [10, 11, 11, 15   , 11, 11, 10],
                         [10,  0,  0, 10   ,  0,  0,  8],
                         [10,  0,  0,  8   ,  0,  0,  8],
                         [10,  0,  0,  8   ,  0,  0,  8],
                         [10, 10, 10,  8   ,  8,  8,  8],
                         [13, 10,  8,  8   ,  8,  8,  8],
                         [ 8,  8,  8,  0   ,  8,  8,  8]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "soi"):
            lst_value = [[11, 15, 50, 99999, 50, 15, 11],
                         [10, 11, 15, 50   , 15, 11, 10],
                         [9 , 10, 11, 15   , 11, 10,  9],
                         [9 , 11, 11, 10   , 12, 12,  9],
                         [8 , 11, 11,  8   , 12, 12,  8],
                         [8 , 11, 11,  8   , 12, 12,  8],
                         [8 ,  8, 10,  8   ,  8,  8,  8],
                         [8 , 12, 13,  8   ,  8,  8,  8],
                         [8 , 12, 12,  0   ,  8,  8,  8]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "cho"):
            lst_value = [[11, 15, 50, 99999, 50, 15, 11],
                         [10, 11, 15, 50   , 15, 11, 10],
                         [9 , 10, 11, 15   , 12, 12,  9],
                         [9 ,  0,  0, 10   ,  10, 11,  9],
                         [8 ,  0,  0, 8    , 10, 11,  8],
                         [8 ,  0,  0, 8    , 10, 11,  8],
                         [8 ,  8,  8, 8    ,  8,  8,  8],
                         [8 ,  8,  8, 8    , 13, 10,  8],
                         [8 ,  8,  8, 0    , 12, 12,  8]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "bao"):
            lst_value = [[14, 15, 50, 99999, 50, 15, 14],
                         [13, 14, 15, 50   , 15, 14, 13],
                         [13, 13, 14, 15   , 14, 13, 13],
                         [12,  0,  0, 15   ,  0,  0, 12],
                         [11,  0,  0, 14   ,  0,  0, 11],
                         [10,  0,  0, 13   ,  0,  0, 10],
                         [ 9,  9,  9, 10   , 10,  9,  9],
                         [ 9,  9,  9, 9    ,  9,  9,  9],
                         [ 9,  9,  9, 0    ,  9,  9,  9]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "ho"):
            lst_value = [[25, 30, 50, 99999, 50, 30, 25],
                         [25, 25, 30, 50   , 30, 25, 25],
                         [18, 20, 20, 30   , 20, 20, 18],
                         [15,  0,  0, 15   , 0 ,  0, 15],
                         [15,  0,  0, 15   , 0 ,  0, 15],
                         [15,  0,  0, 15   , 0 ,  0, 15],
                         [14, 16, 16, 14   , 16, 16, 14],
                         [12, 14, 12, 12   , 12, 12, 12],
                         [10, 12, 12, 0    , 12, 12, 10]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "sutu"):
            lst_value = [[25, 30, 50, 99999, 50, 30, 25],
                         [25, 25, 30, 50   , 30, 25, 25],
                         [18, 20, 20, 30   , 20, 20, 18],
                         [15, 0 ,  0, 15   ,  0,  0, 15],
                         [15, 0 ,  0, 15   ,  0,  0, 15],
                         [15, 0 ,  0, 15   ,  0,  0, 15],
                         [14, 16, 16, 14   , 16, 16, 14],
                         [12, 12, 12, 12   , 12, 14, 12],
                         [10, 12, 12, 0    , 12, 12, 10]]
            
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]
        elif (piece.type.lower() == "voi"):
            lst_value = [[25, 30, 50, 99999, 50, 30, 25],
                         [25, 25, 30, 50   , 30, 25, 25],
                         [18, 20, 20, 30   , 20, 20, 18],
                         [16, 11, 11, 16   , 10, 10, 16],
                         [14, 11, 11, 14   , 10, 10, 14],
                         [12, 11, 11, 12   , 10, 10, 12],
                         [10, 15, 15, 14   , 14, 14, 12],
                         [11, 14, 11, 11   , 11, 11, 11],
                         [11, 11, 11, 0    , 11, 11, 11]]
            if (list_type.lower() == "red"):
                return lst_value[9-piece.position[0]][piece.position[1]-1]
            elif (list_type.lower() == "black"):
                return lst_value[piece.position[0]-1][7-piece.position[1]]

    def lstmove_firsr(self, piece):
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
        ani = piece.type.lower()    # name of animal 
        if ani in ['voi', 'soi', 'cho', 'chuot']:
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
        elif ani in ['sutu', 'ho', 'bao', 'meo']:
            if row == 1:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row+1, col)]
            elif row == 9:  # and not(col in [1,7])
                return [(row, col+1), (row, col-1), (row-1, col)]
            elif row in [2,8] and not (col in [1,7]):
                return [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
            elif row in [3,7] and col == 4:
                return [(row, col+1),(row, col-1),(row+1, col),(row-1, col)]
            elif row in [2,3,7,8] and col == 1:
                return [(row+1, col),(row-1, col),(row, col+1)]
            elif row in [2,3,7,8] and col == 7: 
                return [(row+1, col),(row-1, col),(row, col-1)]
            # can jump through river
            if ani in ['sutu', 'ho', 'bao']:
                if row in [4,5,6] and col == 1:
                    return [(row+1, col),(row-1, col),(row, col+3)]
                elif row in [4,5,6] and col == 7:
                    return [(row+1, col),(row-1, col),(row, col-3)]
                elif row in [4,5,6] and col == 4:
                    return [(row+1, col),(row-1, col),(row, col+3),(row, col-3)]
                if row == 3 and col in [2,3,5,6]:
                    if ani in ['sutu', 'ho']:
                        return [(row, col+1),(row, col-1),(row-1, col),(row+4,col)]
                    else:   # Bao
                        return [(row, col+1),(row, col-1),(row-1, col)]
                elif row == 7 and col in [2,3,5,6]:
                    if ani in ['sutu', 'ho']:
                        return [(row, col+1),(row, col-1),(row+1, col),(row-4,col)]
                    else:   # Bao
                        return [(row, col+1),(row, col-1),(row+1, col)]
            elif ani in ['meo']:
                if row in [4,5,6]: # apply both col = 1 and 7 anh 4
                    return [(row+1, col),(row-1, col)]
                elif row == 3:
                    return [(row, col+1),(row, col-1),(row-1, col)]
                elif row == 7:
                    return [(row, col+1),(row, col-1),(row+1, col)]    

    '''
    - lstmove return list of moves which piece can change state
    - Have checked piece can defeat opposite and conflict with ally
    '''
    def lstmove(self, piece, state):
        lst = self.lstmove_firsr(piece)
        
        if piece.type.lower() in ["ho", "sutu"]:
            check = False
            if piece.position[0] == 3 and piece.position[1] in [2,3,5,6]:
                for x in state.list_black:
                    if x.position[1] == piece.position[1] and x.position[0] in [4,5,6]:
                        i = 0
                        for y in lst:
                            if y[0] == 7:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                for x in state.list_red:
                    if x.position[1] == piece.position[1] and x.position[0] in [4,5,6]:
                        i = 0
                        for y in lst:
                            if y[0] == 7:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
            check = False
            if piece.position[0] == 7 and piece.position[1] in [2,3,5,6]:
                for x in state.list_black:
                    if x.position[1] == piece.position[1] and x.position[0] in [4,5,6]:
                        i = 0
                        for y in lst:
                            if y[0] == 3:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                for x in state.list_red:
                    if x.position[1] == piece.position[1] and x.position[0] in [4,5,6]:
                        i = 0
                        for y in lst:
                            if y[0] == 3:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
            check = False
        
        if piece.type.lower() in ["ho", "sutu", "bao"]:
            check = False
            if piece.position[1] == 1 and piece.position[0] in [4,5,6]:
                for x in state.list_black:
                    if x.position[1] in [2,3] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 4:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                for x in state.list_red:
                    if x.position[1] in [2,3] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 4:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
            check = False
            if piece.position[1] == 4 and piece.position[0] in [4,5,6]:
                for x in state.list_black:
                    if x.position[1] in [2,3] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 1:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                    if x.position[1] in [5,6] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 7:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                for x in state.list_red:
                    if x.position[1] in [2,3] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 1:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                    if x.position[1] in [5,6] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 7:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
            check = False
            if piece.position[1] == 7 and piece.position[0] in [4,5,6]:
                for x in state.list_black:
                    if x.position[1] in [5,6] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 4:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
                for x in state.list_red:
                    if x.position[1] in [5,6] and x.position[0] == piece.position[0]:
                        i = 0
                        for y in lst:
                            if y[1] == 4:
                                lst.pop(i)
                                check = True
                                break
                            i += 1
                        i = 0
                    if check == True:
                        break
            check = False
        
        i = 0
        check = False
        lst_new = []
        if (self.str.lower() == "black"):
            for x in lst:
                for y in state.list_black:
                    if (x[0] == y.position[0]) and (x[1] == y.position[1]):
                        check = True
                        break
                if check == False:
                    lst_new.append(x)
                check = False
            lst = []
            for x in lst_new:
                for y in state.list_red:
                    if (x[0] == y.position[0]) and (x[1] == y.position[1]):
                        if (self.checkDefeat(piece, y)):
                            check = False
                        else:
                            check = True
                        break
                if check == False:
                    lst.append(x)
                check = False      
        elif (self.str.lower() == "red"):
            for x in lst:
                for y in state.list_red:
                    if (x[0] == y.position[0]) and (x[1] == y.position[1]):
                        check = True
                        break
                if check == False:
                    lst_new.append(x)
                check = False
            lst = []
            for x in lst_new:
                for y in state.list_black:
                    if (x[0] == y.position[0]) and (x[1] == y.position[1]):
                        if (self.checkDefeat(piece, y)):
                            check = False
                        else:
                            check = True
                        break
                if check == False:
                    lst.append(x)
                check = False   
        result = []
        for x in lst:
            new = Piece(piece.type, x)
            result.append(new)

        return result

    def next_move(self, state):
        depth = 3
        local_state = copy.deepcopy(state)

        if (self.str.lower() == "black"):
            result = self.alphabeta(local_state, depth, -INF, +INF, True, False)
            for x in state.list_black:
                if x.type == result[2].type:
                    piece = x
                    break
            new_pos = result[2].position
        else:
            result = self.alphabeta(local_state, depth, -INF, +INF, True, True)
            for x in state.list_red:
                if x.type == result[2].type:
                    piece = x
                    break
            new_pos = result[2].position

        return piece, new_pos
        
    def do_move(self, piece, state, player):
        if (player == "red"):
            for x in state.list_red:
                if piece.type == x.type:
                    x.position = piece.position
            i = 0
            for x in state.list_black:
                if piece.position == x.position:
                    state.list_black.pop(i)
                i += 1
        else :
            for x in state.list_black:
                if piece.type == x.type:
                    x.position = piece.position
            i = 0
            for x in state.list_red:
                if piece.position == x.position:
                    state.list_red.pop(i)
                i += 1
        return state

    def alphabeta(self, state, depth, alpha, beta, isPlayer, isAI):
        if depth == 0: #hoac la game over
            return self.evaluatePosition(state), state
        if isAI == True:
            if isPlayer == True:
                maxEval = - INF
                maxState  = None
                maxMove = None
                for item in state.list_red:
                    myList = self.lstmove(item, state)
                    for step in myList:
                        firstState = copy.deepcopy(state)
                        self.do_move(step, firstState, "red")
                        temp = self.alphabeta(firstState, depth - 1, alpha, beta, False, isAI)
                        if temp[0] > maxEval:
                            maxEval = temp[0]
                            maxState = firstState
                            maxMove = step
                        alpha = max(alpha, temp[0])
                        if beta <= alpha: 
                            break
                return maxEval, maxState, maxMove 
            else :
                minEval = +INF 
                minState = None 
                for item in state.list_black:
                    myList = self.lstmove(item, state)
                    for step in myList:
                        firstState = copy.deepcopy(state)
                        self.do_move(step, firstState, "black")
                        temp = self.alphabeta(firstState, depth-1, alpha, beta, True, isAI)
                        if temp[0] < minEval: 
                            minEval = temp[0]
                            minState = firstState 
                        beta = min(beta, temp[0])
                        if beta <= alpha: 
                            break 
                return minEval, minState
        else: # AI is black
            if isPlayer == True:
                maxEval = - INF
                maxState  = None
                maxMove = None
                for item in state.list_black:
                    myList = self.lstmove(item, state)
                    for step in myList:
                        firstState = copy.deepcopy(state)
                        self.do_move(step, firstState, "black")
                        temp = self.alphabeta(firstState, depth - 1, alpha, beta, False, isAI)
                        if temp[0] > maxEval:
                            maxEval = temp[0]
                            maxState = firstState
                            maxMove = step
                        alpha = max(alpha, temp[0])
                        if beta <= alpha: 
                            break
                return maxEval, maxState, maxMove 
            else :
                minEval = +INF 
                minState = None 
                for item in state.list_red:
                    myList = self.lstmove(item, state)
                    for step in myList:
                        firstState = copy.deepcopy(state)
                        self.do_move(step, firstState, "red")
                        temp = self.alphabeta(firstState, depth-1, alpha, beta, True, isAI)
                        if temp[0] < minEval: 
                            minEval = temp[0]
                            minState = firstState 
                        beta = min(beta, temp[0])
                        if beta <= alpha: 
                            break 
                return minEval, minState

