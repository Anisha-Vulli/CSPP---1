'''

Author : Anisha
Date: 01 Aug 2018


'''

NUM = int(input("Enter number"))
I = NUM
print("Hello!")
for I in range(NUM, 0, -2):
    if I%2 == 0:
        print(I)
