'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
import re
def clean_input(string):
    final_stng = ""
    final_stng = re.sub('[^ a-zA-z0-9]','',string)
    # final_stng = (''.join(e for e in string if e.isalnum()))
    return final_stng

def tokenize(string):
    clean_stng = clean_input(string)
    string_obt = clean_stng.split()
    #print(string_obt)
    # len_list = len(string_obt)
    # print(string_obt)
    final = {}
    for i in string_obt:
        final = collections.Counter(string_obt)

    return final
def main():
    range_num = int(input())
    string = ""
    for _ in range(range_num):
        string = string + input()

    print(tokenize(string))

if __name__ == '__main__':
    main()
