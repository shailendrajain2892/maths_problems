import sys

# time complexity O(sqrt(n))
def isPrime(m):
    # base check to see if number is prime or not
    if m == 1:
        return "False"
    if m == 2 or m == 3:
        return "True"
    if m % 2 == 0 or m %3 == 0:
        return "False"
    count=5
    while count*count<=m:
        if m%count==0 or m%(count+2)==0:
            print(f"number : {m} is divisble by {count}")
            return "False"
        count=count+6
    return "True"

if __name__ == "__main__":
    arg = int(sys.argv[1])
    print(isPrime(arg))    