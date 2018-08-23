def mult_matrix(m_1, m_2,n):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    res_mat = []
    for i in range(0,n):
        in_mat = []
        for j in range(0,n):
            sum_val = 0
            for k in range(0,n):
                sum_val = sum_val + (m_1[i][k] * m_2[k][j])
            in_mat.append(sum_val)

        res_mat.append(in_mat)

    return(res_mat)

def add_matrix(m_1, m_2,n):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    res = []
    for i in range(0,n):
        in_mat = []
        for j in range(0,n):
            in_mat.append(m_1[i][j] + m_2[i][j])
        res.append(in_mat)

    return (res)

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    n,m =input().split(',')
    n = int(n)
    
    matrix_1 = []
    for i in range(0,n):
        matrix_1.append(list(map(int,input().split())))

    k,l = input().split(',')
    k = int(k)

    matrix_2 = []
    for j in range(0,k):
        matrix_2.append(list(map(int,input().split())))

    
    for i in matrix_1:
        count = 0
        for j in i:
            count+=1
        if count != m:
            print("Error: Invalid input for the matrix")

    
    for i in matrix_2:
        count = 0
        for j in i:
            count += 1
        if count != l:
            print("Error: Invalid input for the matrix")

    print(add_matrix(matrix_1,matrix_2,n))
    return(mult_matrix(matrix_1,matrix_2,n))
 

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    
    
    
    print(read_matrix())
   




if __name__ == '__main__':
    main()
