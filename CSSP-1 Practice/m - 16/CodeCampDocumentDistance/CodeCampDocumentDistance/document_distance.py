'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def similarity(dict1, dict2, dict3):
    '''
        Compute the document distance as given in the PDF
    '''
    #a = len(dict1)
    num_val = 0
    for i in dict1:
        num_val = dict1[i][0] * dict1[i][1]
    #print(num)
    for j in dict2:
        a_1 = dict2[j] ** 2
    for k in dict3:
        b_1 = dict3[k] ** 2

    distance = (num_val) / math.sqrt(a_1*b_1)
    return distance

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    #print(stopwords)
    return stopwords

def word_list(input1, input2):
    '''Making word list '''
    list_1 = []
    list_2 = []
    key_list = []
    stng_1 = ""
    stng_2 = ""
    stng_1 = re.sub('[^ a-zA-Z0-9]', '', input1.lower())
    stng_2 = re.sub('[^ a-zA-Z0-9]', '', input2.lower())
    stopwords = load_stopwords("stopwords.txt")
    key_list = stopwords.keys()
    #print(key_list)

    list_1 = stng_1.split(" ")
    list_2 = stng_2.split(" ")

    for i in key_list:
        for j in list_1:
            if i == j:
                list_1.remove(j)

    for i in key_list:
        for j in list_2:
            if i == j:
                list_2.remove(j)
    return freq_count(list_1, list_2)

def freq_count(list_1, list_2):
    '''Creating common dictonary '''
    freq_count_dict_1 = {}
    freq_count_dict_2 = {}
    common_dict = {}

    for k in list_1:
        if k not in freq_count_dict_1:
            freq_count_dict_1[k] = 1
        else:
            freq_count_dict_1[k] += 1

    for k in list_2:
        if k not in freq_count_dict_2:
            freq_count_dict_2[k] = 1
        else:
            freq_count_dict_2[k] += 1

    for i in freq_count_dict_1:
        if i in freq_count_dict_2:
            common_dict[i] = [freq_count_dict_1[i], freq_count_dict_2[i]]
        else:
            common_dict[i] = [freq_count_dict_1[i], 0]
            
    for p in common_dict:
        if p not in common_dict:
            common_dict[p] = [0, freq_count_dict_2[p]]

    return(common_dict, freq_count_dict_1, freq_count_dict_2)



def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    (common_dict_1, dict_1, dict_2)= word_list(input1, input2)
    print(similarity(common_dict_1, dict_1, dict_2))

if __name__ == '__main__':
    main()
