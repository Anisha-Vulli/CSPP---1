'''

Author : Anisha Vulli
Date: 07 Aug 2018

'''


def recur_Power(base, exp):
    ''' Calculate power of a number using recursion '''
    ans = 1
    if exp == 0: 
       return 1
    else:
        ans = base * recurPower(base,exp - 1)
        return ans

def main():
    ''' Main function used to take input and print output '''
    data = input()
    data = data.split()
    print(recur_Power(float(data[0]),int(data[1])))   

if __name__ == "__main__":
    main()