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
    def __init__(self,mess,mess):
        self.mess = mess
        self.mess = mess

    def encrypt(self, shift):
        small_letter = ""
        cap_letter = ""
        small_letter = "-" + string.ascii_lowercase  + string.ascii_lowercase 
        cap_letter = "-" + string.ascii_uppercase + string.ascii_uppercase 
        final_code = ""
        length_mess = len(self.mess)
        for i in range[length_mess]:
            if self.mess[i] in small_letter:
                final_code = final_code + small_letter[small_letter.index(self.mess[i] + shift)]

            elif self.mess[i] in cap_letter:
                final_code = final_code + cap_letter[cap_letter.index(self.mess[i] + shift)]
            else:
                final_code = final_code + self.mess[i]

        print(final_code)



### Paste your implementation of the mess class here
        

def main():
    '''
        Function to handle testcases
    '''
    mess_input = input()
    mess_shift = int(input())
    # c = Message_encry.encrypt(mess_input, mess_shift)
    print(Message_encry.encrypt(mess_input, mess_shift))
    

if __name__ == "__main__":
    main()
