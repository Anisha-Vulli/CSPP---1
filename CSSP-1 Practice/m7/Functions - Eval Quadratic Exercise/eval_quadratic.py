# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
#that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.

'''
Author: Anisha Vulli
Date: 07 Aug 2018
'''

def eval_quadratic(a_in, b_in, c_in, x_in):
    ''' Function to calculate the result of the quadratic equation '''
    return (a_in*(x_in**2))+ (b_in*x_in) + c_in

def main():
    ''' Main function to take inputs and print outputs '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for i in range(len(data)):
        temp = str(data[i]).split('.')
        if temp[1] == '0':
            data[i] = int(float(str(data[i])))
        else:
            data[i] = data[i]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
