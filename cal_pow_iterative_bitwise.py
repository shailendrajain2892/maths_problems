import sys


def cal_pow_bit(x, n):
    res=1
    while n > 0:
        if n%2 != 0:
            res=res*x
        x=x*x
        n=n//2
    return res

if __name__ == "__main__":
    x = int(sys.argv[1])
    n = int(sys.argv[2])
    print(cal_pow_bit(x, n))
