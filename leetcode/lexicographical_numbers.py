'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
'''


class Solution:
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
print(Solution().lexicalOrder(n))