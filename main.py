
import imp
import time
# ======================================================================


class Piece:
    def __init__(self, animal, pos):
        self.type = animal
        self.position = pos

    def __str__(self):
        return str(self.type) + ': ' + str(self.position)


class Board:
    def __init__(self, l_black=[], l_red=[]):
        self.list_black = l_black
        self.list_red = l_red

    def print(self):
        print('blacks: ')
        for item in self.list_black:
            print(item)
        print('\nreds: ')
        for item in self.list_red:
            print(item)
        print()


# ======================================================================

# Student SHOULD implement this function to change current state to new state properly
def doit(move, board):
    new_state = Initial_Board
    return new_state


# ======================================================================
list_blacks = [Piece('Voi', (7, 7)), Piece('SuTu', (9, 1)), Piece('Ho', (9, 7)),
               Piece('Bao', (7, 3)), Piece('Soi', (7, 5)), Piece('Cho', (8, 2)),
               Piece('Meo', (8, 6)), Piece('Chuot', (7, 1))]
list_red = [Piece('Voi', (3, 1)), Piece('SuTu', (1, 7)), Piece('Ho', (1, 1)),
              Piece('Bao', (3, 5)), Piece('Soi', (3, 3)), Piece('Cho', (2, 6)),
              Piece('Meo', (2, 2)), Piece('Chuot', (3, 7))]
Initial_Board = Board(list_blacks, list_red)
# ======================================================================


def play(student_a, student_b, start_state=Initial_Board):
    player_a = imp.load_source(student_a, student_a + ".py")
    player_b = imp.load_source(student_b, student_b + ".py")

    a = player_a.Player('black')
    b = player_b.Player('red')

    curr_player = a
    state = start_state

    board_num = 0

    state.print()

    while True:
        print("It is ", curr_player, "'s turn")

        start = time.time()
        move = curr_player.next_move(state)
        elapse = time.time() - start

        # print(move)

        if not move:
            break

        print("The move is : [", move[0].type, ': ', move[0].position, '-> ', move[1], end="] ")
        print(" (in %.2f ms)" % (elapse*1000), end=" ")
        if elapse > 3.0:
            print(" ** took more than three second!!", end=" ")
            break
        print()
        # check_move
        state = doit(move, state)

        board_num += 1
        print('board num = ', board_num)
        state.print()

        if curr_player == a:
            curr_player = b
        else:
            curr_player = a

    print("Game Over")
    if curr_player == a:
        print("The Winner is:", student_b, 'red')
    else:
        print("The Winner is:", student_a, 'black')


play("co_thu", "co_thu")
