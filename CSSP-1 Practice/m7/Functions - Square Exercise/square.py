# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.
'''
Author : Anisha Vulli
Date: 07 Aug 2018

'''
def square(x_in):
    ''' Function to calculate square of the number '''
    ans = 1
    ans = x_in * x_in
    return ans
def main():
    ''' Main function to take input and print output values '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
