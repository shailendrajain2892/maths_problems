import sys


def kth_bit_set(n, k):
    n = n>>(k-1)
    if n & 1 != 0 :
        return True
    else :
        return False

def kth_bit_set_2(n, k):
    m = pow(2, k-1)
    if m & n != 0 :
        return True
    else:
        return False
    
if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(kth_bit_set(n, k))
    print(kth_bit_set_2(n, k))
