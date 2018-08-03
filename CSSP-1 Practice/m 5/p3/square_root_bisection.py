'''

Author : Anisha Vulli
Date : 03 Aug 2018

'''
def main():
    ''' Function to find square root through bisection'''
    s_q = input()
    ep_i = 0.01
    #s_p = 0.1
    num_gu = 0
    l_o = 0
    h_i = int(s_q)
    gu_ess = (l_o + h_i)/2.0
    while abs(gu_ess**2 - int(s_q)) >= ep_i:
        num_gu += 1
        if gu_ess ** 2 < int(s_q):
            l_o = gu_ess
        else:
            h_i = gu_ess
        gu_ess = (l_o + h_i)/2.0
    print(gu_ess)
    #print(num_gu)

if __name__ == "__main__":
    main()
