'''

Author: Anisha Vulli
Date : 24th Aug 2018

'''
def is_diagonal_forward(board, turn):
    '''Checking diagonal forward '''
    count_val = 0
    for lop_1 in range(3):
        if board[lop_1][lop_1] is turn:
            count_val += 1
    if count_val == 3:
        #print("DF true")
        return True
    return False

def is_diagonal_backward(board, turn):
    '''Checking diagonal backward '''
    count_val = 0
    in_loop = 2
    for lop_1 in range(3):
        if board[lop_1][in_loop] is turn:
            count_val += 1
        in_loop -= 1

    if count_val == 3:
        #print("DB true")
        return True
    return False

def is_horizontal(board, turn):
    '''Check horizontal '''
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if board[lop_1][in_loop] is turn:
                count_val += 1
        if count_val == 3:
            #print("horizontal true")
            return True
        count_val = 0
    return False

def is_vertical(board, turn):
    '''Check vertical '''
    count_val = 0
    for lop_1 in range(3):
        for in_loop in range(3):
            if not board[in_loop][lop_1] is turn:
                count_val += 1
        if count_val == 0:
            #print("vertical true")
            return True
        count_val = 0
    return False

def read_input():
    '''Reading the input '''
    board = []
    for _ in range(0, 3):
        board.append(list(map(str, input().split())))

    #print(board)

    return board


def main():
    '''Main function '''
    board = read_input()
    #print(board)
    count_val = 0
    x_count = 0
    o_count = 0
    char_count = 0
    other_count = 0
    basic_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'x':
                x_count += 1
                basic_count += 1
            elif board[i][j] == 'o':
                o_count += 1
                basic_count += 1
            elif board[i][j] == '.':
                char_count += 1
                #basic_count += 1
            else:
                other_count += 1
                #basic_count += 1

    #print(x_count, o_count, char_count, other_count)
    #print(basic_count)

    if other_count != 0:
        print("invalid input")
        count_val += 1

    elif x_count > o_count + 1 or o_count > x_count + 1:
        print("invalid game")

    elif basic_count == 9:
        print("draw")

    else:
        turn_x = 'x'
        boolean_x = (is_vertical(board, turn_x) or is_horizontal(board, turn_x)
                     or is_diagonal_forward(board, turn_x)
                     or is_diagonal_backward(board, turn_x))

        #print(boolean_x)
        turn_o = 'o'
        boolean_o = (is_vertical(board, turn_o) or is_horizontal(board, turn_o)
                     or is_diagonal_forward(board, turn_o)
                     or is_diagonal_backward(board, turn_o))
        #print(boolean_o)

        if boolean_x and boolean_o and count_val == 0:
            print("invalid game")
            count_val += 1

        if boolean_x and count_val == 0:
            print(turn_x)
            count_val += 1

        if boolean_o and count_val == 0:
            print(turn_o)
            count_val += 1

if __name__ == '__main__':
    main()
