'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''Reading multiple lines and printing them '''
    number_lines = int(input())
    final_stng = ""
    temp_stng = ""
    for _ in range(number_lines):
        temp_stng = input() + '\n'
        final_stng = final_stng + temp_stng

    print(final_stng)


if __name__ == '__main__':
    main()
