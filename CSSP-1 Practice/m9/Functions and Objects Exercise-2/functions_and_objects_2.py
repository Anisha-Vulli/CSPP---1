#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]


def incre(k):
	s = k + 1
	return s
def apply_to_each(L):
    li = []
    s = 0
    for j in L:
    	li. append(incre(j))
    return li


def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1))

if __name__ == "__main__":
    main()
