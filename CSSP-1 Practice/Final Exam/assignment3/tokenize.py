'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
def clean_input(string):
    final_stng = ""
    final_stng = (''.join(e for e in string if e.isalnum()))
    return final_stng

def tokenize(string):
    string_obt = string.split()
    clean_stng = clean_input(string_obt)
    print(clean_stng)
    # len_list = len(string_obt)
    # print(string_obt)
    # final = []
    # for i in range(len_list):
    #     final[i] = collections.Counter(string_obt[i])

    #return final
def main():
    range_num = int(input())
    for _ in range(range_num):
        print(tokenize(input()))

if __name__ == '__main__':
    main()
