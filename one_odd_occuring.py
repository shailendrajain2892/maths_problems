# TC - O(2n)
# SC - O(n)
def find_one_odd_occuring_dict(n):
    d = {}
    for i in n:
        if i not in d:
            d[i]=1
            # print(d)
        else:
            d[i]+=1
    odd_numbers=[]
    for i, j in d.items():
        if j%2 != 0:
            odd_numbers.append(i)
    return odd_numbers
# naive Solution 
# TC - O(n2)
# SC - O(1)
def find_one_odd_occuring_naive(n):
    for i in n :
        count=0
        for j in n: 
            if i==j:
                count+=1
        if count%2==1:
            return i
    
"""
Using the property of xor 
x^0 = x
x^y = y^x (associative)
x^(y^z) = (x^y)^z
so if x is even then 
x^x^x^x = 0 
if odd
x^x^x=x
using this propery 
if do xor of all the number in a list only number which is odd will remain and rest will become zero
in below example : 
4^4^7^8^8^7^6 --> (4^4)^(8^8)^(7^7)^6 --> 6
#TC --> O(n)
#SC --> O(1)
"""
def find_one_odd_occuring(n):
    res=0
    for i in n:
        res = res^i
    return res 

if __name__ == "__main__":
    n_l = [4, 4, 7, 8, 8, 7, 6, 3, 3, 12]
    print(find_one_odd_occuring(n_l))
    # print(find_one_odd_occuring_naive(n_l))
    # print(find_one_odd_occuring_dict(n_l))