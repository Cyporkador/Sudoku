import random

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def solve(bo):
    if not valid_board(bo):
        return False
    else:
        find = find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        one_to_nine = scramble([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for i in one_to_nine:
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return bo
                else:
                    bo[row][col] = 0
        return False


def isSolved(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            if bo[i][j] == 0:
                return False
    return valid_board(bo)


def scramble(orig):
    new = orig[:]
    random.shuffle(new)
    return new


# does not count duplicates of 0
def check_duplicates(l):
    if len(l) == 0:
        return False
    else:
        checking = l[0]
        new_list = l[:]
        del new_list[0]
        for item in new_list:
            if checking == item and checking != 0:
                return True
        return check_duplicates(new_list)


def valid_board(bo):
    for row in bo:
        if check_duplicates(row):
            return False

    for i in range(0, 9):
        column = []
        for j in range(0, 9):
            column.append(bo[j][i])
        if check_duplicates(column):
            return False

    minigrids = [[bo[0][0], bo[0][1], bo[0][2], bo[1][0], bo[1][1], bo[1][2], bo[2][0], bo[2][1], bo[2][2]],
                 [bo[0][3], bo[0][4], bo[0][5], bo[1][3], bo[1][4], bo[1][5], bo[2][3], bo[2][4], bo[2][5]],
                 [bo[0][6], bo[0][7], bo[0][8], bo[1][6], bo[1][7], bo[1][8], bo[2][6], bo[2][7], bo[2][8]],
                 [bo[3][0], bo[3][1], bo[3][2], bo[4][0], bo[4][1], bo[4][2], bo[5][0], bo[5][1], bo[5][2]],
                 [bo[3][3], bo[3][4], bo[3][5], bo[4][3], bo[4][4], bo[4][5], bo[5][3], bo[5][4], bo[5][5]],
                 [bo[3][6], bo[3][7], bo[3][8], bo[4][6], bo[4][7], bo[4][8], bo[5][6], bo[5][7], bo[5][8]],
                 [bo[6][0], bo[6][1], bo[6][2], bo[7][0], bo[7][1], bo[7][2], bo[8][0], bo[8][1], bo[8][2]],
                 [bo[6][3], bo[6][4], bo[6][5], bo[7][3], bo[7][4], bo[7][5], bo[8][3], bo[8][4], bo[8][5]],
                 [bo[6][6], bo[6][7], bo[6][8], bo[7][6], bo[7][7], bo[7][8], bo[8][6], bo[8][7], bo[8][8]]]
    for grid in minigrids:
        if check_duplicates(grid):
            return False
    return True


def valid(bo, num, pos):
    # check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for j in range(len(bo[0])):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == len(bo[0]) - 1:
                if bo[i][j] == 0:
                    print(" ")
                else:
                    print(bo[i][j])
            else:
                if bo[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def generate_new_board():
    new_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 9):
        new_board[i] = board[i][:]
    for i in range(0, 9):
        row = random.randint(0, 8)
        new_board[i][row] = i + 1
    new_board = solve(new_board)
    original = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(0, 9):
        original[i] = new_board[i][:]
    for i in range(0, 9):
        for j in range(0, 9):
            hide = random.randint(0, 99)
            if hide < 55:
                new_board[i][j] = 0
    return [new_board, original]
