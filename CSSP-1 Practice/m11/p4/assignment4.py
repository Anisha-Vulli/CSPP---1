'''

Author: Anisha Vulli
Date: 10 Aug 2018

'''

def calculate_hand_len(hand):
    ''' Hand length function '''   
    return len(hand)

def main():
    ''' Main function '''
    n_in = input()
    a_dict = {}
    for i in range(int(n_in)):
        data = input()
        l = data.split()
        a_dict[l[0]] = int(l[1])
    print(calculate_hand_len(a_dict))
        


if __name__ == "__main__":
    main()