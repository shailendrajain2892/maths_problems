from math import sqrt
import math
import sys
# from prime import isPrime


def exactly3divisor(n):
    count=0
    if n < 4:
        return count
    for i in range(4, n+1):
        divcount=0
        # print(f"checking for {i}")
        for j in range(1, i+1):                    
            if i%j==0:
                # print(f"{i} is div by {j}")
                divcount+=1
        if divcount == 3:
            count+=1
        # else:
            # print(f"divcount is : {divcount}")
    return count

def isPrime(n):
    N = int(math.sqrt(n))+1
    if n == 1: 
        return False
    for i in range(2, N):
        print(f"checking for {i}")
        if n%i==0:
            return False
        print(f"{n} is not div by {i}")
    return True

def optimizedExactly3Divisor(n):
    N = int(sqrt(n))
    print(f"sqrt is {N}")
    count=0
    for i in range(2, N+1):
        if isPrime(i):
            print(f"{i} is prime")
            count+=1
        else:
            print(f'{i} no prime')
    return count

if __name__ == "__main__":
    num = int(sys.argv[1])
    # print(exactly3divisor(num))
    print(optimizedExactly3Divisor(num))

