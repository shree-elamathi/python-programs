#Given an array of integers, calculate the ratios of its elements that are positive, negative,
# and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
# though answers with absolute error of up to  are acceptable.
def plusminus(arr):
    n=len(arr)
    plus=0
    minus=0
    zero=0
    for i in arr:
        if 0<i:
            plus+=1
        elif i==0:
            zero+=1
        else:
            minus+=1
    print(round(plus/n,6))
    print(round(minus/n,6))
    print(round(zero/n,6))
arr = [-4, 3, -9, 0, 4, 1]
plusminus(arr)