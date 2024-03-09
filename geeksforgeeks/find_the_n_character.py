#Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01
# and 1 becomes 10. Find the nth character (considering 0 based indexing) of the string after
# performing these r iterations.
def nthchar(s,r,n):
    for i in range(0,r):
        a=""
        for i in s:
            if i=="1":
                a+="10"
            else:
                a+="01"
        s=a
    return (s[n])
s="111101"
r=2
n=3
print(nthchar(s,r,n))
#another method
#corr = {
#            '1': '10',
#            '0': '01'
#        }
#
#        r = 1 << r
#
#        while r > 1:
#            index = n // r
#            s = corr[s[index]]
#            if n >= r:
#                n = n % r
#            r = r // 2
#       return s[n//r]
