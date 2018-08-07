'''

Author: Anisha Vulli
Date: 07 Aug 2018.

'''
def factorial_fun(n_in):
    ''' Calculating the factorial of the number '''
    if (n_in == 0) or (n_in == 1):
        return 1
    return n_in * factorial_fun(n_in - 1)
def main():
    ''' Main function is used to take input and output '''
    num_in = input()
    print(factorial_fun(int(num_in)))

if __name__ == "__main__":
    main()
