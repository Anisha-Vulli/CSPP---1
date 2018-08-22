#define the gen_primes function here
def genPrimes(n):
    i = 2
    cou = 0
    while cou<n:
        f = 0
        for item in range(1, i):
            if i % item == 0: 
                f += 1
        if f == 1:
            yield i
            cou += 1
        i += 1
def main():
    n = int(input())
    prime_gen = genPrimes(n)
    for i in range(n):
        p = prime_gen.__next__()
        print(p)
    
    
if __name__ == "__main__":
    main()
