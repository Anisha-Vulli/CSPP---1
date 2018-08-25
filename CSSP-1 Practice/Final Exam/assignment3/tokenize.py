'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import collections
def tokenize(string):
    string_obt = string
    final = {}
    for i in string:
        final = collections.Counter(string)

    return final
def main():
    range_num = int(input())
    for _ in range(range_num):
        print(tokenize(input()))

if __name__ == '__main__':
    main()
