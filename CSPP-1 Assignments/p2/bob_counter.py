'''

Author : Anisha Vulli
Date : 02 Aug 2018

'''

def main():
   '''This function is used to count number of times bob occured '''
   s_tr = input()
   cou_nt = 0
   for i in range(0,len(s_tr)-2):
       if(s_tr[i] == 'b' and s_tr[i+1] == 'o' and s_tr[i+2] == 'b'):
           cou_nt += 1
   print(cou_nt)

if __name__== "__main__":
    main()
