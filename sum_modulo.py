# 9223372036854775807 9223372036854775807
import sys


def sumUnderModulo(a,b):
    # code here
    return (a+b)%(pow(10, 9)+7)

def multiplication(a, b):
    return (a*b)%(pow(10, 9)+7)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(sumUnderModulo(a, b))
    print(multiplication(a, b))