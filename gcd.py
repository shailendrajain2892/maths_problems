import argparse
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time} seconds to execute.")
        return result
    return wrapper

# greatest common divisior 
# time complexity - BigO(min(a,b))
@timing_decorator
def gcd(m, n):
    print(m, n)
    res=min(m, n)
    while (res>0):
        if (n%res==0 and m%res==0):
            break
        else:
            res = res-1
    return res

# Euclidean Algo naive approch
@timing_decorator
def euclidean_algo(m, n):
    while(m != n):
        if (m>n):
            m=m-n
        else:
            n=n-m
    return m

@timing_decorator
def euclidean_algo_opt(m, n):
    if n == 0:
        return m
    else:
        return euclidean_algo(n, m%n) 
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Find GCD(Greatest Common Divisor) for a given numbers')
    parser.add_argument('-m','--num1', help='Description for input argument', required=True, type=int)
    parser.add_argument('-n','--num2', help='Description for output argument', required=True, type=int)
    args = vars(parser.parse_args())
    m = args.get('num1')
    n = args.get('num2')
    # print(gcd(m, n))
    # print(euclidean_algo(m,n))
    print(euclidean_algo_opt(m,n))