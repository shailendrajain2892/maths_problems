import math
import sys


def primer_factors(m):
    pm_list=[]
    counter=2
    while m!=1:
        if m%counter==0:
            pm_list.append(counter)
            m=m//counter
        else:
            counter+=1
        print(counter)
    return pm_list

def primer_factors2(n):
    l=[]
    # check if number is 2 or 3
    if n == 2 or n == 3: 
        return n
    # check divisibility by 2 and 3
    while (n % 2 == 0):
        l.append[2]
        n=n//2
    while (n%3 == 0):
        l.append[3]
        n=n//3
    
    # now start the check from 5 till sqrt(n) and increment by 6
    for i in range(5,int(math.sqrt(n)), 6):
        print(i)
        while (n%i==0):
            print(f"{n} is divisible by {i}")
            l.append(i)
            n=n//i
        while(n%(i+2)==0):
            l.append(i+2)
            n=n//(i+2)
    if n>3:
        l.append(n)
    return l
        
if __name__ == "__main__":
    num = int(sys.argv[1])
    print(primer_factors2(num))

