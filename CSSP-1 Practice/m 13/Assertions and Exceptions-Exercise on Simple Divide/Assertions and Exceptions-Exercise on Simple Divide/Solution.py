#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    return item / denom
def fancy_divide(list_of_numbers, index):
    try:
        denom = list_of_numbers[index]
        return [simple_divide(item, denom) for item in list_of_numbers]

    except ZeroDivisionError:
        print("We cannot divide with zero")
        denom = 1
        return [simple_divide(item, denom) for item in list_of_numbers]
def main():
    data = input()
    l=data.split()
    l1=[]
    for j in l:
        l1.append(float(j))
    s = input()
    index=int(s)
    print (fancy_divide(l1,index))
    

if __name__== "__main__":
    main()
