#You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1) and
# return the result as an unsigned integer.
def fliping(n):
    binary1=format(n,'032b')
    binary2=""
    for i in binary1:
        if i=='1':
            binary2+=str(0)
        else:
            binary2+=str(1)
    val=int(binary2,2)
    return val
n=9
print(fliping(n))