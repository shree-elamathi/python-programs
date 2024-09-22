'''
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
'''
class Solution:
    def findKthNumber(self, n, k):
        res=self.lexicalOrder(n)
        return res[k-1]
    def lexicalOrder(self, n: int):
        result = []
        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_number = current * 10 + i
                if next_number > n:
                    break
                dfs(next_number)
        for i in range(1, 10):
            if i > n:
                break
            dfs(i)

        return result

n = 13
k = 2
print(Solution().findKthNumber(n,k))