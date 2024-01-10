import sys

# time complexity O(sqrt(n))
def isPrime(m):
    # base check to see if number is prime or not
    if m == 1:
        return "No Prime"
    if m == 2 or m == 3:
        return "Not prime"
    if m % 2 == 0 or m %3 == 0:
        return "No Prime"
    count=5
    while count*count<=m:
        if m%count==0 or m%(count+2)==0:
            print(f"number : {m} is divisble by {count}")
            return "Not Prime"
        count=count+6
    return "Prime"

if __name__ == "__main__":
    arg = int(sys.argv[1])
    print(isPrime(arg))    