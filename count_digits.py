# without using len function 
# time complexity O(logn) or theta(number of digits in n )
def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

# using len function
def count_digits2(n):
    return len(str(n))



if __name__ == '__main__':
    print(count_digits(123))
    print(count_digits(12345))
    print(count_digits(100))
    print("*"*50)
    print(count_digits2(123))
    print(count_digits2(12345))
    print(count_digits2(100))
