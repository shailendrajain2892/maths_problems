import math
import sys


def isPrime(n):
    if n == 1 : 
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# naive approach with time complexity of n*(n*1/2)
def find_all_primes(n):
    prime_list=[]
    for i in range(2, n):
        if isPrime(i):
            prime_list.append(i)

# optimized approach with time complexity of O(nloglogn)
def o_find_all_primes(n):
    prime_list=[True]*n
    prime_num = []
    for i in range(2, n):
        if prime_list[i]:
            prime_num.append(i)
            for j in range(i*i, n, i):
                prime_list[j]=False
    print(f"{len(prime_num)} prime numbers")
    return prime_num

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(o_find_all_primes(num))
