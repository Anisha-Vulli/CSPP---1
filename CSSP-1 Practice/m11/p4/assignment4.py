'''

Author: Anisha Vulli
Date: 10 Aug 2018

'''

def calculate_hand_len(hand):
    ''' Hand length function '''
    
    hand_list = list(hand.values())
    #print(hand_list)
    sum_val = 0
    #print(hand.values())
    for i in hand_list:
        sum_val = sum_val +i
    return sum_val

def main():
    ''' Main function '''
    n_in = input()
    a_dict = {}
    for i in range(int(n_in)):
        data = input()
        l_i = data.split()
        a_dict[l_i[0]] = int(l_i[1])
    print(calculate_hand_len(a_dict))



if __name__ == "__main__":
    main()
