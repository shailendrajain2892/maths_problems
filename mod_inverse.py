import sys


def modInverse(a,m):
    ##Your code here
    for i in range(m):
        if a*i%m == 1:
            return i
        
if __name__ == "__main__":
    a = int(sys.argv[1])
    m = int(sys.argv[2])
    print(modInverse(a, m))