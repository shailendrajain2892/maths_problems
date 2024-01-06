import sys


# time complexity theta(digits of number)
def isPalindrome(s):
    return s == s[::-1]

def isPalindrome2(pn):
    opn=pn
    npn=[]
    if pn<10:
        return True
    while pn>0:
        npn.append(str(pn%10))
        pn=pn//10
    npn = int("".join(map(str, npn)))
    if opn == npn:
        return True
    else:
        return False
    
def isPalindrome3(pnumber):
    temp = pnumber
    if pnumber < 10:
        return True
    reverse = 0
    while temp > 0:
        remainder = temp%10
        reverse = (reverse*10)+remainder
        temp = temp//10
    if reverse == pnumber:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(isPalindrome2(int(sys.argv[1])))
    print(isPalindrome3(int(sys.argv[1])))