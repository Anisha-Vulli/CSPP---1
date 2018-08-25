def valid_game(board):
    x_count = 0
    o_count = 0
    sum_val = 0
    for i in board:
        x_count += i.count('x')
        o_count += i.count('o')
        sum_val = i.count('x') + i.count('o') + i.count('.')
    if sum_val != 9:
        print("invalid input")
        return

    if(x_count - o_count in  (0, 1, -1)):
        return "invalid game"

    return True


def check_horizontal(board):
    for i,j in enumarate(board):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

def check_vertical(board):
    for i,j in enumarate(board):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[i][0]

def check_diagonal(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

def check_game(board):
    count = 0
    for i,j in enumarate(board):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            count += 1

    for i,j in enumarate(board):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            count += 1

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        count += 1

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        count += 1

    if count > 1:
        print("invalid game")
    else:
        return True

def check_winner(board):
    winner_horz = check_horizontal(board)
    winner_vert = check_vertical(board)
    winner_diag = check_diagonal(board)
    if (winner_horz and winner_vert) or (winner_horz and winner_diag) or (winner_vert and winner_diag):
        return "invalid input"
    if winner:
        return board

    if winner:
        return board

    if winner:
        return board
    else:
        return "draw"

def main():
    board = []

    for _ in range(3):
        board.append(input().split())

    if valid_game(board) and check_game(board):
        print(check_winner(board))


if __name__ == '__main__':
    main()
