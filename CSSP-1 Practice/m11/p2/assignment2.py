'''
#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has no side effects: i.e.,
it must not mutate the hand passed in.
Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py.

Author : Anisha Vulli
Date : 10 Aug 2018

'''
def update_hand(hand, word):
    ''' Update hand function '''
    given_word = word
    given_dict = hand
    #updated_dict = {}

    #hand_length = 7
    for i in given_word:
        if i in given_dict:
            given_dict[i] -= 1

    return given_dict

def main():
    ''' Main function '''
    num_in = input()
    adict = {}
    for i in range(int(num_in)):
        data = input()
        l_i = data.split()
        adict[l_i[0]] = int(l_i[1])
        i += 1
    data1 = input()

    print(update_hand(adict, data1))


if __name__ == "__main__":
    main()
