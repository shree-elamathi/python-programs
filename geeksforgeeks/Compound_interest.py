P=eval(input("Enter the Principle amount:"))
R=eval(input("Enter the Rate of interest:"))
T=eval(input("Enter the Time span:"))
A=P*(1+R/100)**T
Compound_interest=A-P
print("The compound interest is:",Compound_interest)
