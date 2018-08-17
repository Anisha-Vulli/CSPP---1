import re

def word_list(input1, input2):
    list_1 = []
    list_2 = []
    stng_1 = ""
    stng_2 = ""
    stng_1 = re.sub('[^ a-zA-Z0-9]','',input1.lower())
    stng_2 = re.sub('[^ a-zA-Z0-9]','',input2.lower())

    list_1 = stng_1.split(" ")
    list_2 = stng_2.split(" ")

    return list_1, list_2

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(word_list(input1, input2))

    #print(similarity(input1, input2))

if __name__ == '__main__':
    main()
