import sys


def power_of_2(n):
    if n <= 1: 
        return False
    if n & n-1 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(power_of_2(n))