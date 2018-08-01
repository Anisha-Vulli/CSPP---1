'''

Author : Anisha
Date: 01 Aug 2018


'''

NUM = int(input("Enter number"))
I = NUM
for I in range(0, NUM, 2):
    if I%2 == 0:
        print(I)
print("Good bye!")
