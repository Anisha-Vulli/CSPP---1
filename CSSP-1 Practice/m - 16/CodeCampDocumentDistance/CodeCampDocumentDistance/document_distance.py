'''
    Document Distance - A detailed description is given in the PDF
'''
import re

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    pass

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

# def remove_words(list_1, list_2):
#   new_list = []
#   new_list = load_stopwords(stopwords.txt)
#   print(new_list.keys())

def word_list(input1, input2):
    list_1 = []
    list_2 = []
    key_list = []
    stng_1 = ""
    stng_2 = ""
    stng_1 = re.sub('[^ a-zA-Z0-9]','',input1.lower())
    stng_2 = re.sub('[^ a-zA-Z0-9]','',input2.lower())
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
            
    #print(stng_1)
    freq_count(list_1, list_2)
    # dict_1 = dict(list_1)
    # print(dict_1)

    #return list_1, list_2

def freq_count(list_1, list_2):
    freq_count_dict_1 = {}
    freq_count_dict_2 = {}
    common_dict = {}
    sum_val = 0
    sum_val_1 = 0

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
            common_dict[i] = [freq_count_dict_1[i],0]
            
    for p in common_dict:
        if p not in common_dict:
            common_dict[p] = [0,freq_count_dict_2[p]]

    #print(sum_val)
    #print(sum_val_1)
    print(common_dict)
    #print(freq_count_dict_1)
    # print(freq_count_dict_2)



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
