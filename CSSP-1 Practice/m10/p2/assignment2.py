'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!!!")
    print("The secret word was guessed")
    print("There are only 8 guesses")
    strng = "abcdefghijklmnopqrstuvwxyz"
    word = random.choice(wordlist)
    a = list(word)
    print("------------------------------------------------------------")
    temp_stng = ""
    for char in word:
        temp_stng = temp_stng + "-"

    print (temp_stng)
    b=list(temp_stng)
    word_guess = 1
    
    guess = 8
    while guess >= 1:
        n = input("Enter the guess letter")
        if n in a:
             #temp_stng = temp_stng.replace(each_char,"_")
             strng = strng.replace(n, "")
             print(strng)   
             word_guess += 1
             for j in range(len(word)):
                if word[j] == n:
                    b[j] = n
             print(''.join(b)) 
             print("-------")
           
        else:
            guess -= 1
            strng = strng.replace(n, "")
            print(strng)
            print("You have only" + " " +str(guess))
            for j in range(len(word)):
                if word[j] == n:
                    b[j] = n
            print(''.join(b)) 
            print("Oops!! Wrong guess babe...")
            print("-------")
        
        if word_guess == len(word) - 1:

            break
    print("You lost!!! I am sorry")
    print("The word was" + " " + word)
              
    return temp_stng



def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    #print("This is the word" + random.choice(wordlist))

    #hangman(secretWord)
    #print(random.choice(wordlist))
    #print("The guessed word" + temp_stng)



if __name__ == "__main__":
    main()
