import sys


def sumCountSetBits(n):
    # code here
    # return the count
    # base case
    if n==0:
        return 0

    # count most significant bit
    msb_count=0
    while 1<<msb_count<=n:
        msb_count+=1
    msb_count-=1

    #calculate total 1s till msb number
    k = pow(2, msb_count)
    tc=(k/2)*msb_count

    # calculate total 1s for remainder
    tc+=(n-k+1)+sumCountSetBits(n-k)

    return tc


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(sumCountSetBits(n))