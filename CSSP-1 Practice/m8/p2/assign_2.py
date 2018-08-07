'''

Author : Anisha Vulli
Date: 07 Aug 2018

'''

def sum_of_digits(n_in):
    ''' Function is used to caluculate sum of digits'''
    if n_in == 0:
        return n_in
    return n_in%10 + sum_of_digits(n_in//10)


def main():
    ''' Main function to take input and print output '''
    num_in = input()
    print(sum_of_digits(int(num_in)))

if __name__ == "__main__":
    main()
