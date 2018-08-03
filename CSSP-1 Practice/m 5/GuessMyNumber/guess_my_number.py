'''

Author : Anisha Vulli
Date : 03 Aug 2018

'''
def main():
    ''' This function is used to make guess'''
    print("Guess a number between 1 and 100")
    l_o = 0
    h_i = 100
    m_i = (l_o + h_i)//2
    s_1 = ''

    while s_1 != 'c':
        
        if s_1 == 'h':
            l_o = m_i
            m_i = (l_o + h_i)//2
             
        if s_1 == 'l':
            h_i = m_i
            m_i = (l_o + h_i)//2
        
        print("Is your number greater than M ?")
        print("Mid number is: " + str(m_i))      
        print("Enter h : high l: low and c: correct")

        s_1 = input()

    print("Number is : " + str(m_i))   	    

if __name__== "__main__":
	main()