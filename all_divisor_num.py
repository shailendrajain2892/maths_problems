import math
import sys

from prime import isPrime


def all_div_num(n):
    div = []
    div2 = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            div.append(i)
    # div4 = div.reverse()
    for i in div[::-1]:
        if n//i != i:
            div2.append(n//i)
    div3 = div + div2
    return div3

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(all_div_num(n))