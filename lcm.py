# least common multiple 
# a=4, b=6 o/p - 12
import argparse
from functools import reduce
from gcd import euclidean_algo_opt

def lcm(a, b):
    max_num = max(a, b)
    res = max_num
    while True:
        if res%a == 0 and res%b ==0:
            return res
        res=res+max_num
    return res

def lcm_opt(a, b):
    return abs(a*b)/euclidean_algo_opt(a,b)
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Find GCD(Greatest Common Divisor) for a given numbers')
    parser.add_argument('-m','--num1', help='Description for input argument', required=True, type=int)
    parser.add_argument('-n','--num2', help='Description for output argument', required=True, type=int)
    args = vars(parser.parse_args())
    m = args.get('num1')
    n = args.get('num2')
    print(lcm_opt(m,n))