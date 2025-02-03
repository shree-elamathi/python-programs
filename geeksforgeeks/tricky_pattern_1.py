'''
WAP to print below pattern
for n = 6
1
2 4
3 5 7
6 8 10 12
9 11 13 15 17
14 16 18 20 22 24
'''
class Solution:
    def pattern1(self, n):
        odd = 1
        even = 2
        count = 1
        for i in range(n):
            for j in range(count):
                if i%2 == 0:
                    print(odd, end=" ")
                    odd += 2
                else:
                    print(even, end = " ")
                    even += 2
            count += 1
            print()


n = 3
Solution().pattern1(n)
