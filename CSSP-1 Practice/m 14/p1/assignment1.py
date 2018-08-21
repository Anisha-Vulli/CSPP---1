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
    '''For encrypting data'''
    def __init__(self, data):
        '''For message encryption'''
        self.data = data
        #print(self.data)

    def encrypt(self, shift):
        '''Message encryption shifted output'''
        small_letter = ""
        cap_letter = ""
        small_letter = "-" + string.ascii_lowercase  + string.ascii_lowercase
        cap_letter = "-" + string.ascii_uppercase + string.ascii_uppercase
        final_code = ""
        #length_data = len(self.data)
        for i in range(0, len(self.data)):
            if self.data[i] in small_letter:
                final_code = final_code + small_letter[small_letter.index(self.data[i]) + shift]

            elif self.data[i] in cap_letter:
                final_code = final_code + cap_letter[cap_letter.index(self.data[i]) + shift]
            else:
                final_code = final_code + self.data[i]

        return final_code



### Paste your implementation of the data class here

def main():
    '''
        Function to handle testcases
    '''
    data_input = input()
    data_shift = int(input())
    # c = dataage_encry.encrypt(data_input, data_shift)
    message_encry_obj = Message_encry(data_input)
    print(message_encry_obj.encrypt(data_shift))


if __name__ == "__main__":
    main()
