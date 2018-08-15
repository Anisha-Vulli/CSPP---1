'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_four_of_a_kind(hand):
    '''
    This code is  to check if the given hand is
    four of a kind or not.

    Converted the hand into a list of indexes and calculated
    the difference between the consicutive numbers.
    If the difference is equal to four then we can say that it is

    '''

    stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(stng_values.index(i[0]))

    hand_values.sort() #For the sorting the indexes in hand.
    #print(hand_values)
    count_diff = 1

    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count_diff += 1

    return count_diff == 4
        


def is_full_house(hand):
    '''

    The hand is said to be inn full house if the three cards
    are either 3 or 6.

    '''
    #stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(i[0])

    hand_values.sort()
    #print(hand_values)

    count = 1

    for i in hand_values:
        if i in (3, 6):
            count += 1

    return count == 3

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(stng_values.index(i[0]))

    hand_values.sort()

    #print(hand_values)

    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] != -1:
            return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    values_set = set({})

    for i in hand:
        values_set.add(i[1])

    #print(values_set)

    return len(values_set) == 1



def is_three_pair(hand):
    '''
    This code is  to check if the given hand is
    four of a kind or not.

    Converted the hand into a list of indexes and calculated
    the difference between the consicutive numbers.
    If the difference is equal to three then we can say that it is

    '''

    stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(stng_values.index(i[0]))

    hand_values.sort() #For the sorting the indexes in hand.
    #print(hand_values)
    count_diff = 1

    #print(hand_values)

    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count_diff += 1

    return count_diff == 3
        

def is_two_pair(hand):
    ''' Sees if the hand is a two pair or not '''
    hand_values = [f for f, s in hand]
    values = set(hand_values)
    twopairs = [f for f in values if hand_values.count(f) == 2]
    return len(twopairs) == 2

def is_one_pair(hand):
    '''
    This code is  to check if the given hand is
    four of a kind or not.

    Converted the hand into a list of indexes and calculated
    the difference between the consicutive numbers.
    If the difference is equal to three then we can say that it is

    '''

    stng_values = "--23456789TJQKA"
    hand_values = []

    for i in hand:
        hand_values.append(stng_values.index(i[0]))

    hand_values.sort() #For the sorting the indexes in hand.
    count_diff = 1

    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] == 0:
            count_diff += 1

    return count_diff == 2
        

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    hand_rank_value = 0

    if is_straight(hand) and is_flush(hand):
        hand_rank_value = 8
    elif is_four_of_a_kind(hand):
        hand_rank_value = 7
    elif is_full_house(hand):
        hand_rank_value = 6
    elif is_flush(hand):
        hand_rank_value = 5
    elif is_straight(hand):
        hand_rank_value = 4
    elif is_three_pair(hand):
        hand_rank_value = 3
    elif is_two_pair(hand):
        hand_rank_value = 2
    elif is_one_pair(hand):
        hand_rank_value = 1
    else:
        hand_rank_value = 0
    return hand_rank_value

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)

    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    #print(HANDS)

    #print(is_flush(HANDS))
