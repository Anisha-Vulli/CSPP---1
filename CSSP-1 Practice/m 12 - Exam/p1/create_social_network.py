'''
    Assignment-1 Create Social Network
'''

def create_social_network(data_in):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    a_dict = {}
    list_1 = []
    for i in data_in:
        list_1 = i.split("follows")
        #print(list_1[1])
        #print(list_1)
        if list_1[0] in a_dict:
            list_1[1] = list_1[1].split(',')
            a_dict[list_1[0]] = ','.join(list_1[1])
            '''for j in list_1[1]:
                a_dict[list_1[0]] = ','.join(list_1[1])'''
            
            
        else:
            list_1[1] = list_1[1].split(',')
            a_dict[list_1[0]] = ','.join(list_1[1])
            
            
        
    return a_dict

    

def main():
    '''
        handling testcase input and printing output
    '''
    lines_num = int(input())
    string_in = ''
    for i in range(lines_num):
        string_in += input()
        if i != (lines_num - 1):
            string_in += '\n'
        i += 1
    string_1 = string_in.split('\n')
    
    #print(string_1)
    
    print(create_social_network(string_1))

if __name__ == "__main__":
    main()
