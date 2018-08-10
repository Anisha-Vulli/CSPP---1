# Assignment-3
'''

Author : Anisha Vulli
Date : 10 Aug 2018


'''

def is_valid_word(word, hand, word_list):
    ''' Valid word function '''
    #word_list = list(word)
    j = 0
    k = 0
    for i in word:
        if i in hand:
            j += 1
    print(j)

    if word in word_list:
        k = 1

    return bool((j == len(word)) and (k == 1))

def main():
    ''' Main program '''
    word = input()
    n_in = int(input())
    adict = {}
    for i in range(n_in):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
        i += 1
    l_2 = input().split()
    print(is_valid_word(word, adict, l_2))

if __name__ == "__main__":
    main()
