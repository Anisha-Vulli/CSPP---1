def is_diagonal_forward(board, turn):
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if not board[lop_1][lop_1] is turn:
                count_val += 1
        if count_val == 0:
            return True
        count_val = 0
    return False

def is_diagonal_backward(board, turn):
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if not board[lop_1][in_loop] is turn:
                count_val += 1
            in_loop -= 1
        if count_val == 0:
            return True
        count_val = 0
    return False

def is_horizontal(board, turn):
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if board[lop_1][in_loop] is not turn:
                count_val += 1
        if count_val == 0:
            return True
        count_val = 0
    return False

def is_vertical(board, turn):
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if not board[in_loop][lop_1] is turn:
                count_val += 1
        if count_val == 0:
            return True
        count_val = 0
    return False

def read_input():
    board = []
    for i in range(0, 3):
        board.append(list(map(str, input().split())))

    print(board)

    return board


def main():
    '''Main function '''
    board = read_input()
    count_val = 0

    turn_x = 'x'
    boolean_x = (is_vertical(board, turn_x) or is_horizontal(board, turn_x) 
                 or is_diagonal_forward(board, turn_x) 
                 or is_diagonal_backward(board, turn_x))
    #print(boolean_x)
    turn_o = 'o'
    boolean_o = (is_vertical(board, turn_o) or is_horizontal(board, turn_o) 
                 or is_diagonal_forward(board, turn_o) 
                 or is_diagonal_backward(board, turn_o))

    if boolean_x and count_val == 0:
        print(turn_x)
        count_val += 1

    if boolean_o and count_val == 0:
        print(turn_o)
        count_val += 1

if __name__ == '__main__':
    main()
