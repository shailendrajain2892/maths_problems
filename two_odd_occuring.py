def find_two_odd_occuring(n):
    x=0
    for i in n:
        x = x^i
    print(f"x value is :{x}")
    k = x&(~(x-1))
    res1=0
    res2=0
    for i in n:
        if i&k != 0:
            res1=res1^i
        else:
            res2=res2^i
    return res1, res2

if __name__ == "__main__":
    n_l = [4, 4, 7, 7, 8, 8, 3, 3, 13, 13, 19, 6]
    print(find_two_odd_occuring(n_l))