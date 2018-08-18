'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
import copy

def similarity(dict1):
    '''
        Compute the document distance as given in the PDF
    '''
    #a = len(dict1)
    num_val = 0
    a_1 = 0
    b_1 = 0
    distance = 0
    for i in dict1:
        num_val += dict1[i][0] * dict1[i][1]
        a_1 += dict1[i][0] ** 2
        b_1 += dict1[i][1] ** 2
    #print(num)
    # for j in dict2:
    #     a_1 += dict1[] ** 2
    # for k in dict3:
    #     b_1 += dict3[k] ** 2

    distance = (num_val) / (math.sqrt(a_1) * math.sqrt(b_1))
    return distance

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''

    stopwords = {}
    with open(file_name, 'r') as file_name:
        for line in file_name:
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
    stng_1 = re.sub('[^ a-z]', '', input1.lower())
    stng_2 = re.sub('[^ a-z]', '', input2.lower())
    #print(stng_1,stng_2)
    stopwords = load_stopwords("stopwords.txt")
    key_list = list(stopwords.keys())
    #print(key_list)

    list_1 = stng_1.split(" ")
    list_2 = stng_2.split(" ")
   
    #print(list_1,list_2)
    word_list_1 = list_1[:]
    for i in word_list_1:
        if i in key_list:
            list_1.remove(i)

    word_list_2 = list_2[:]
    for i in word_list_2:
        if i in key_list:
            list_2.remove(i)

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

    for p_1 in freq_count_dict_2:
        if p_1 not in common_dict:
            common_dict[p_1] = [0, freq_count_dict_2[p_1]]

    d_1 = copy.deepcopy(common_dict)

    for h_1 in d_1:
        len_1 = len(h_1)
        if len_1 == 0:
            del common_dict[h_1]

    return common_dict

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    common_dict_1 = word_list(input1, input2)
    print(similarity(common_dict_1))

if __name__ == '__main__':
    main()
