'''

Author : Khyathi C

Date: 2-8-18

'''
def main():
    ''' This code is used to find the longest substring in the given string'''
    str_1 = input()
    str_2 = ''
    f_s = ''
    leng = len(str_1)
    f_max = 0
    f_count = 0
    f_s = str_1[0]
    for i in range(0, leng-1):
        if ord(str_1[i]) <= ord(str_1[i+1]):
            f_count += 1
            f_s = f_s + str_1[i+1]
        else:
            if f_count > f_max:
                f_max = f_count
                str_2 = f_s
            f_count = 0
            f_s = str_1[i+1]
    if f_count > f_max:
        str_2 = fs
    print(str_2)

if __name__ == "__main__":
    main()
