import sys

# naive approach theta(n)
def cal_pow(x, y):
    if y == 0:
        return 1
    res = x
    for i in range(1, y):
        res*=x
    return res 

# optimized approach where we calculate power based on following:
# if x, n --> if n is even --> x*(n/2) + x*(n/2)
            #   if n odd --> x*(n/2) + x
# time complexiy for this algo is O(logn) 
def o_cal_pow(x, n):
    res = x
    # if n%2 == 0:
    n = n*0.5
    for i in range(1, n):
        res*=x
    if n%2==0:
        return res*res
    else:
        return res*x
    
# recursive approach
def o_r_calc_pow(x, n):
    if n == 0:
        return 1
    tmp = o_r_calc_pow(x, n%2) 
    tmp = tmp*tmp
    if n%2 == 0:
        return tmp 
    else:
        return tmp*x


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(cal_pow(x, y))