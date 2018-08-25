'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    temp_keys = sorted(dictionary.keys())
    temp_dict = {}
    for key in temp_keys:
    	if key in temp_dict:
    		temp_dict[key].append('#' * dictionary[key])
    	else:
    		temp_dict[key] = '#' * dictionary[key]


    print(temp_dict)
    keys = sorted(temp_dict.keys())

    for key in keys:
        print(key, "-", dictionary[key])

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
