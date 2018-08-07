'''


Author: Anisha Vulli
Date: 07 Aug 2018

'''

def iter_power(base, exp):
    ''' Power of a number caluculation using iteration'''
    ans = 1
    while exp > 0:
        ans = ans * base
        exp -= 1
    return ans
def main():
    ''' Main function used to read input and print output '''
    base_num = input()
    exp_num = input()
    print(iter_power(int(base_num), int(exp_num)))

if __name__ == "__main__":
    main()
