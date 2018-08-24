def print_board(board):
    board_list = board
    for i in range(len(board_list)):
        return join(board_list[i])




def read_input():
    board = []
    for i in range(0, 3):
        board.append(list(map(input().split())))

    print(print_board)


def main():
    '''Main function '''
    
    read_input()

if __name__ == '__main__':
    main()
