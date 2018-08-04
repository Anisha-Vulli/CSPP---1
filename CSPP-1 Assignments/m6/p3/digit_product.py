'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''
    Finding product of all digits
    '''
    int_input = int(input())
    #count_i = 0
    n_i = 0
    d_i = 0
    pro_o = 1
    if int_input != 0:
        if  int_input > 0:
            n_i = int_input
            while n_i > 0:
                d_i = n_i % 10
                n_i = n_i //10
                pro_o = pro_o * d_i
            print(pro_o)
        else:
            n_i = -(int_input)
            while n_i > 0:
                d_i = n_i % 10
                n_i = n_i //10
                pro_o = pro_o * d_i
            print(-(pro_o))

    else:
        print(0)

if __name__ == "__main__":
    main()
