import sys


def count_trailing_zeros(n):
    count = 0
    while (n%10 == 0):
        count+=1
        n = n//10
        # print(count, remainder, n)
    return count

def count_trailing_zeros_using_primefactorization(n):
    res = 0
    i=5
    while (i<=n):
       res = res + n//i
       i=i*5
    return res

def fact(n):
    ft = 1
    for i in range(1, n+1):
        ft*=i
    return ft


if __name__ == '__main__':
    # print(count_trailing_zeros(fact(int(sys.argv[1]))))
    print(count_trailing_zeros_using_primefactorization(int(sys.argv[1])))