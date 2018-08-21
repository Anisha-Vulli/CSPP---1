''' 

Author: Anisha Vulli
Date: 21 Aug 2018


'''
import string
# Helper code
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list

WORDLIST_FILENAME = 'words.txt'
# Helper code End


class Message_encry():
    def __init__(self, data):
        self.message = data

    def encrypt(self, shift):
        small_letter = ""
        cap_letter = ""
        small_letter = "-" + string.ascii_lowercase  + string.ascii_lowercase 
        cap_letter = "-" + string.ascii_uppercase + string.ascii_uppercase 
        final_code = ""
        for i in range[0, len(self.message)]:
            if self.message[i] in small_letter:
                final_code = final_code + small_letter[small_letter.index(self.message[i] + shift)]

            elif self.message[i] in cap_letter:
                final_code = final_code + cap_letter[cap_letter.index(self.message[i] + shift)]
            else:
                final_code = final_code + self.message[i]

        return final_code



### Paste your implementation of the Message class here
        

def main():
    '''
        Function to handle testcases
    '''
    data_input = input()
    data_shift = int(input())
    print(Message_encry.encrypt(data_input, data_shift))
    

if __name__ == "__main__":
    main()
