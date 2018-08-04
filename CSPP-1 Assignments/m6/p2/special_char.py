'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters

Author: Anisha Vulli
Date: 04 Aug 2018

'''
def main():
    '''
    Put spaces in place of special characters
    '''
    str_input = input()
    str_output = ""
    #a = {'!','@','#','$','%','^','&','*'}
    for char in str_input:
        if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '*':
            str_output = str_output + " "
        else:
           str_output = str_output + char
    print(str_output)

if __name__ == "__main__":
    main()
