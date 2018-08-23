def mult_matrix(m_1, m_2,n,m,k,l):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    if m == k:
        res_mat = []
        for i in range(0, n):
            in_mat = []
            for j in range(0, m):
                sum_val = 0
                for k in range(0,n):
                    sum_val = sum_val + (m_1[i][k] * m_2[k][j])
                in_mat.append(sum_val)
            res_mat.append(in_mat)

        return(res_mat)

    else:
        print("Error: Matrix shapes invalid for mult")




def add_matrix(m_1, m_2, n,m,k,l):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if n == k and m == l:
        res = []
        for i in range(0, n):
            in_mat = []
            for j in range(0, m):
                in_mat.append(m_1[i][j] + m_2[i][j])
            res.append(in_mat)
        return (res)

    else:
        print("Error: Matrix shapes invalid for addition")



    

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
    m = int(m)
    matrix_1 = []
    for i in range(0, n):
        matrix_1.append(list(map(int, input().split())))

    k,l = input().split(',')
    k = int(k)
    l = int(l)

    matrix_2 = []
    for j in range(0, k):
        matrix_2.append(list(map(int, input().split())))

    #print(l)
    flag = True
    for i in matrix_1:
        count = 0
        for j in i:
            count+=1
        if count != m:
            flag = False
            
    if flag == False:
        print("Error: Invalid input for the matrix")
    
    flag = True
    for i in matrix_2:
        count = 0
        for j in i:
            count += 1
        if count != l:
            flag = False
            
    if flag == False:
        print("Error: Invalid input for the matrix")
            

    if flag == True:
        print(add_matrix(matrix_1, matrix_2,n,m,k,l))
        print(mult_matrix(matrix_1, matrix_2,n,m,k,l))


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()

if __name__ == '__main__':
    main()
