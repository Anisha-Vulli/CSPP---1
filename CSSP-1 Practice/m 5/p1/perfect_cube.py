'''

Author : Anisha Vulli
Date : 03 Aug 2018

'''

def main():
    ''' This function is used to caluclate cube root through guess and check '''
    #print("Enter an integer")
    x_i = input()
    res = 0
    while res**3 < int(x_i):
        res = res + 1
    if res**3 == int(x_i):
        print(str(x_i) + " is a perfect cube")
    else:
        print(str(x_i) + " is not a perfect cube")
if __name__ == "__main__":
    main()
