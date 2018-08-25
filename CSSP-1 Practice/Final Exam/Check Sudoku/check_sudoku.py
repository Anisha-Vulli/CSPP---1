'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_inside(list_sudoku):
    temp = list_sudoku
    #print(temp)
    temp_list = []
    basic_list = []
    empty_list = []
    count_vert = 0
    count_hori = 0
    j = 0
    for val in temp_list:
        empty_list = sorted(i)
        if empty_list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count_hori += 1

    empty_list = []
    temp_list = []
    basic_list = []

    for i in range(9):
        basic_list.append(temp[i][j])
        j += 1
        temp_list.append(basic_list)

    for i in temp_list:
        empty_list = sorted(i)
        if empty_list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count_vert += 1

    return count_vert == 9 and count_hori == 9



def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    list_sudoku = sudoku
    basic_list = []
    count = 0
    
    for i in list_sudoku:
        basic_list = sorted(i)
        if basic_list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count += 1

    if count == 9 and check_inside(list_sudoku):
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()