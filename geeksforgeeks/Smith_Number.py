class solution:
    def smithnum(self,n):
        a=str(n)
        dig=[]
        lhs=0
        for i in a:
            dig.append(int(i))
        for j in dig:
            lhs=lhs+j
        rhs=prime_factors_of_number(n)
        if lhs==rhs:
           return 1
        else:
           return 0

#def factors(number):
#   import sympy
#   prd=0
#   prime_factors = sympy.factorint(number)
#   factors_list = []
#   for factor, power in prime_factors.items():
#       factors_list.extend([factor] * power)
#   for i in factors_list:
#       prd=prd+i
#   return prd
def prime_factors_of_number(number):
    factors = []
    divisor = 2
    prd=0
    while number > 1:
        while number % divisor == 0:
            factors.append(str(divisor))
            number //= divisor
        divisor += 1
    if len(factors)<2:
        return 0
    for i in factors:
        if len(i)==1:
            prd=prd+int(i)
        else:
            for j in i:
                prd=prd+int(j)
    return prd

print(solution().smithnum(985))