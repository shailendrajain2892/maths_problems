import sys


def termOfGp(A, B, N):
    common_ratio = B/A
    nterm = A*pow(common_ratio, N-1)
    return nterm

if __name__ == "__main__":
    A = int(sys.argv[1])
    B = int(sys.argv[2])
    N = int(sys.argv[3])
    print(termOfGp(A, B, N))