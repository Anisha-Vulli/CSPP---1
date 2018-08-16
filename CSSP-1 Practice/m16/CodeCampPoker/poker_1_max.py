def hand_values(hand):
    ''' Returns the hand values based on the index '''
    return sorted(set(["--23456789JQKA".index(f) for f,s in hand]), reverse = True)

def is_straight(ranks):
    ''' Check if straight or not ''' 
    return(len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4) or (ranks[1:5] == [5,4,3,2] and rank[0] == 14 ) 

def is_flush(hand):
    ''' Check if it is flush '''
    values_set = set({})
    for i in hand:
        values_set.add(i[1])
    return len(values_set) == 1

def which_kind(ranks,n):
    ''' Returning the rank and checking of the repetition and sending the rank''' 
    for i in rank:
        if rank.count(i) == n:
        return i
def is_two_pair(ranks):
    '''Checking if two pair or not '''
    high_val = kind(rank,2)
    low_val = sorted(kind(rank, 2))
    if high_val != low_val:
        return high_val, low_val, ranks

def hand_rank(hand):
    ''' Function to call all the functions '''
    rank = hand_values(hand)

    if is_straight(hand) and is_flush(hand):#Straightflush
        return 8, rank
    if which_kind(rank,4):#Four of a kind
        return 7, which_kind(rank, 4), rank
    if which_kind(rank, 3) and which_kind(rank, 2):#Full house
        return 6, which_kind(rank, 3), which_kind(rank, 2), rank
    if is_flush(hand):#Flush
        return 5, rank
    if is_straight(hand):#Straight
        return 4, rank
    if which_kind(rank, 3):# Three of a kind
        return 3, which_kind(rank, 3), rank
    if is_two_pair(rank): #Two pair
        return 2, is_two_pair(rank)
    if which_kind(rank, ): #One pair
        return 1, which_kind(rank, 2), rank
  
    return 0, rank

def poker(hands):
    '''
    This function is to return the max code
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    list_1 = []
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)

    print(' '.join(poker(HANDS)))
