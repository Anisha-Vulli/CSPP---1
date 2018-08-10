'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score for a single word.
The function get_word_score should accept as input a string of lowercase letters (a word) and
return the integer score for that word, using the game's scoring rules.

Author : Anisha Vulli
Date : 10 Aug 2018

'''

def get_word_score(word, num_letters):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    scrabble_letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

    enter_word = word
    hand_size = num_letters
    #values_list = list(scrabble_letter_values.values())
    #print(values_list)
    score_of_word = 0
    sum_of_letters = 0
    for i in enter_word:
        sum_of_letters = sum_of_letters + scrabble_letter_values[i]
        #score = score + values_list[b]

    score_of_word = sum_of_letters * len(enter_word)

    if hand_size == len(enter_word):
        score_of_word = score_of_word + 50

    return score_of_word


def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
