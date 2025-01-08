def GCD(m,n):
    #base case to have remainder as 1
    rem = 1
    if m>n:
        # the largest val will be dividend and the other will be divisor
        divd = m
        divs = n
    else:
        divd = n
        divs = m
    # the loop is executed till the remainder becomes 0
    while rem !=0:
        rem = divd % divs
        #even after this if the rem is not 0 then replace the divd and divs
        if rem != 0:
            divd = divs
            divs = rem
    return divs

x=eval(input("Enter the 1st number: "))
y=eval(input("Enter the 2nd number: "))
print("GCD is",GCD(x,y))
