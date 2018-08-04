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
    count_i = 0
    n = 0
    d = 0
    pro_o = 1
    if n>0:
        n = int_input
        while n>0:
            d = n % 10
            n = n //10
            pro_o = pro_o * d
        print(pro_o)
    else:
        n = -(int_input)
        while n>0:
            d = n % 10
            n = n //10
            pro_o = pro_o * d
        print(-(pro_o))


if __name__ == "__main__":
    main()
