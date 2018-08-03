'''

Author: Anisha Vulli
Date: 03 Aug 2018

'''

def main():
    ''' This function is used to calcualte square root '''
    s_q = input()
    ep_i = 0.01
    gu_ess = 0.0
    inc_e = 0.001
    while abs(gu_ess ** 2 - int(s_q)) >= ep_i and gu_ess <= int(s_q):
        gu_ess += inc_e
    if abs(gu_ess ** 2 - int(s_q)) >= ep_i:
        print('Failed on cube root of' + str(s_q))
    else:
        print(gu_ess, 'is close to the cube root of', str(s_q))

if __name__ == "__main__":
    main()
