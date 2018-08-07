'''

Author : Anisha Vulli
Date : 07 Aug 2018

'''


def gcd_recur(a_in, b_in):
    temp_var = 0
    lim = min(a_in,b_in)
    if lim == a_in:
    	temp_var = a_in
    	a_in = b_in
    	b_in = temp_var
    if a_in%b_in == 0:
    	return b_in
    return gcd_recur(b_in, a_in%b_in)


def main():
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]),int(data[1])))

if __name__ == "__main__":
    main()