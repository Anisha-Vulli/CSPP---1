'''

Author : Anisha
Date : 02 Aug 2018


'''


def main():
    '''
    Function main() is used to count vowels in the string

    '''
    st_r = input()
    cou_nt = 0
    for ch_ar in st_r:
        if ch_ar in ('a', 'e', 'i', 'o', 'u'):
            cou_nt += 1
    print(cou_nt)

if __name__ == "__main__":
    main()
