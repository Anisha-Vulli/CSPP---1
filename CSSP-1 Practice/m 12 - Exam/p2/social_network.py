'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''

def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    if arg1 in netwok:
        network[arg1].append(arg2)
    return network


def unfollow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    if arg1 in netwok:
        network[arg1].remove(arg2)
    return network

def delete_person(network, arg1):
    '''
        2 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 is a person in the network
        delete_person function is called when arg1 wants to exit from the network
        so, this should result in deleting arg1 from network
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the network dictionary and return it
    '''
    
    for person in network:
        if person in network[arg1]:
            network[person].remove(arg1)

    if arg1 in network:
        del network[arg1]
    return network


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
            #string_1 = line.split(' ')
            network = delete_person(network, output[1])
        i += 1

    print(network)

if __name__ == "__main__":
    main()
