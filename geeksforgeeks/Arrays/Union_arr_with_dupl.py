'''
You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

'''


class Solution:
    def findUnion(self, a, b):
        res = []
        Dict = {}
        for i in a:
            if i not in Dict:
                Dict[i] = 1
                res.append(i)

        for i in b:
            if i not in Dict:
                Dict[i] = 1
                res.append(i)

        return res

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(Solution().findUnion(a,b))
