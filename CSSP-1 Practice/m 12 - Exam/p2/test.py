def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    a_dict = {}
    list_1 = []

    if arg1 in a_dict.keys():
        for j in a_dict[arg1]:
            list_1[1] = list_1[1].split(',')
            a_dict[list_1[0]] = list_1[j]
    else:
        a_dict.setdefault(arg1,arg2)
        

    return a_dict

def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            string_1 = line.split(' ')
            network = follow(network, string_1[1], string_1[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])
        i += 1

    print(network)