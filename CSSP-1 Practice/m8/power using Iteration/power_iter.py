'''

Author : Anisha Vulli
Date : 07 Aug 2018

'''
def iterPower(base, exp):
    '''Caluculate power using iteration '''
    ans = 1
    while exp>0:
        ans = ans * base
        exp -= 1
    return ans
    


def main():
    ''' Main function which is used to take inputs  '''
    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()