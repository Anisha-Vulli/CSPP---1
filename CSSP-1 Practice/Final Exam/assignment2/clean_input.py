'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
#import re
def clean_string(string):
    '''Cleaning a string '''
    final_stng = ""
    #final_stng = re.sub('[^a-zA-z0-9]','',string)
    final_stng = (''.join(e for e in string if e.isalnum()))
    return final_stng

def main():
    '''Input a string '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
