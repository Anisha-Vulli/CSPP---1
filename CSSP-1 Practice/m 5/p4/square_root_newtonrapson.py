'''

Author : Anisha Vulli
Date : 03 Aug 2018

'''

def main():
    ''' Square root calculation using newton raphson'''
    nu_m = input()
    ep_i = 0.01
    int_num = int(nu_m)
    gu_ess = int_num/2.0
    while abs(gu_ess*gu_ess - int_num) >= ep_i:
        gu_ess = gu_ess - (((gu_ess**2) - int_num)/(2*gu_ess))
    print(str(gu_ess))

if __name__ == "__main__":
    main()
