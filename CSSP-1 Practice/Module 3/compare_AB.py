'''
Author : Anisha
Date : 01 Aug 2018


'''

VARA = int(input("Enter something"))
VARB = int(input("Enter something"))
if isinstance(VARA, str) or isinstance(VARB, str):
    print("Strings involved")
if VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("Equal")
else:
    print("smaller")
