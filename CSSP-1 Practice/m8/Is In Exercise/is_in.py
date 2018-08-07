''' 

Author: Anisha Vulli
Date: 07 Aug 2018

'''

def isIn_2(char_in,a_Str):
    sorted_aStr = sorted(a_Str)
    x = isIn(0,len(sorted_aStr),char_in,sorted_aStr)
    return x

def isIn(min_val,max_val,char,a_Str):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = (min_val+max_val)//2
    if a_Str[mid] == char:
        return "True"
    elif mid == min_val or mid == max_val:
        return "False"
    else:
        if a_Str[mid] > char:
            return isIn(min_val,mid,char,a_Str)
        elif a_Str[mid] < char:
            return isIn(mid,max_val,char,a_Str)

def main():
    data = input()
    data = data.split()
    print(isIn_2(data[0], data[1]))


if __name__ == "__main__":
    main()