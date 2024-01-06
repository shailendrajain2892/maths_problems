import math
import sys

# time complexity theta(n)
def find_factorial(n):
    fact=1
    while(n>0):
        fact*=n
        n=n-1
    return fact

def recur_fact(n):
    if n==1 or n==0:
        return 1
    return n*recur_fact(n-1)

def loop_fact(n):
    fact=1
    for i in range(1, n+1):
        fact = fact*i
    return fact 

def count_digit_fact(n):
    sum = 0
    for i in range(1, n+1):
        sum+=math.log10(i)
    sum = math.floor(sum)
    return sum+1

if __name__ == "__main__":
    print(find_factorial(int(sys.argv[1])))
    print(recur_fact(int(sys.argv[1])))
    print(loop_fact(int(sys.argv[1])))
    print(count_digit_fact(int(sys.argv[1])))
    