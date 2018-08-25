'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
import re
def clean_input(string):
    '''Cleaning string '''
    final_stng = ""
    final_stng = re.sub('[^ a-zA-z0-9]', ' ', string)
    #final_stng = (''.join(e for e in string if e.isalpha()))
    #print(final_stng)
    return final_stng

def tokenize(string):
    '''Dictonary of words and their frequencies '''
    clean_stng = clean_input(string)
    string_obt = clean_stng.split()
    temp_list = []
    final_dict = {}
    for _ in string_obt:
        temp_list = collections.Counter(string_obt)

    for _, doc in enumerate(temp_list):
        if doc in final_dict:
            final_dict[doc].append(temp_list[doc])
        else:
            final_dict[doc] = temp_list[doc]

    return final_dict
def main():
    '''Main function '''
    range_num = int(input())
    string = ""
    for _ in range(range_num):
        string = string + input()

    print(tokenize(string))

if __name__ == '__main__':
    main()
