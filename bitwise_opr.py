import sys


def and_bitwise_opr(x, y):
    return x&y

def or_bitwise_opr(x, y):
    return x|y

def xor_bitwise_opr(x, y):
    return x^y

def left_shift_opr(x, y):
    return x<<y

def right_shift_opr(x, y):
    return x>>y

def bitwise_not(x):
    return ~x

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(and_bitwise_opr(x, y)) 
    # 3 -- 0 1 1
    # 6 -- 1 1 0
    # & --> 0 1 0 --> 2 (output) multiply 
    print(or_bitwise_opr(x, y))
    # | --> 1 1 1 --> 7 (output) add bits 
    print(xor_bitwise_opr(x, y))
    # ^ --> 1 0 1 --> 5 (output) if bits are differnent then 1 otherwise 0
    print(left_shift_opr(x, y))
    # output can be represented by x*(2^y) 
    print(right_shift_opr(x, y))
    # output can be represnted by x//(2^y)
    print(bitwise_not(x))
    """
    for unsinged number that means for all +ve numbers 
    range is 0 to 2^32-1 --> 4294967296 -1 --> 4294967295
    in bitwise not it invert each and everbit 
    so for ~1 == 2^32-1-1 this will be output 
    for signed number range is -2^31 to 2^31 -1
    so it's here 2^32 -1 is rep as -1 so ouput becomes -1 -1 --> -2 for 1
    """

    