# without using len function 
# time complexity O(logn) or theta(number of digits in n )
import math
import sys


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

# using len function
def count_digits2(n):
    return len(str(n))

def count_digits3(n):
    if n>1:
        cd = math.log10(n)
        print(cd)
        return math.floor(cd)+1
    else:
        return 1



if __name__ == '__main__':
    print(count_digits3(int(sys.argv[1])))
