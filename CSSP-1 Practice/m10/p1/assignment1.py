'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    ''' letters that are not present are '''
    temp_stng = "abcdefghijklmnopqrstuvwxyz"
    for each_char in letters_guessed:
        temp_stng = temp_stng.replace(each_char, "")
    return temp_stng


def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
