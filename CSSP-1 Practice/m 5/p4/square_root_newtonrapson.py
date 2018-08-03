'''

Author : Anisha Vulli
Date : 03 Aug 2018

'''

def main():
	nu_m = input()
	ep_i = 0.01
	y = int(nu_m)
	gu_ess = y/2.0
	while abs(gu_ess*gu_ess - y) >= ep_i:
		gu_ess = gu_ess - (((gu_ess**2) - y)/(2*gu_ess))
	print(str(gu_ess))

if __name__== "__main__":
	main()
