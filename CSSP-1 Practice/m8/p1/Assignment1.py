'''

Author: Anisha Vulli
Date: 07 Aug 2018.

'''
def factorial_fun(n):
    ''' Calculating the factorial of the number '''
    if (n == 0) or (n == 1):
       return 1
    else:
       return n * factorial_fun(n - 1)
       

def main():
    num_in = input()
    print(factorial_fun(int(num_in)))    

if __name__ == "__main__":
    main()
