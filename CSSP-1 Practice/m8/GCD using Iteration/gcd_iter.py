'''

Author: Anisha Vulli
Date : 07 Aug 2018

'''

def gcd_iter(a_num1, b_num2):
    ''' Calculate the GCD of two numbers '''
    lim = min(a_num1, b_num2)
    for i in range((lim + 1), 1, -1):
        if (a_num1%i == 0) and (b_num2%i == 0):
            return i
    return 0


def main():
    ''' Main function used to take input and output '''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
