import sys

# naive method
def count_set_bits(n):
    res = 0
    while n > 0:
        if n%2 == 1: # n&1 == 1 (can also be written as this if last bit is set then output will be 1)
            res=res+1

        n=n//2
    return res

def count_set_bits_brian_kerningams_algo(n):
    res = 0
    while n > 0 :
        res+=1
        n = n & (n-1)
    return res

# assuming we have 32 bit number 
def count_set_bits_lookup_tables(n):
    tbl = []
    tbl.append(0)
    for i in range(1, 256):
        indx = i&i-1
        tbl.append(tbl[i&i-1]+1)
    return tbl[n&255]+tbl[n>>8 & 255]+tbl[n>>16 & 255]+tbl[n>>24]

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(count_set_bits(n))
    print(count_set_bits_brian_kerningams_algo(n))
    print(count_set_bits_lookup_tables(n))
