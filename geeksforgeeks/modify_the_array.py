'''
Given a single linked list, calculate the sum of the last n nodes.
Note: It is guaranteed that n <= number of nodes.
'''
class Solution:
    def modifyAndRearrangeArr (self, arr) :
        n=len(arr)
        for i in range(n-1):
            if arr[i]!=0 and arr[i]==arr[i+1]:
                arr[i]=arr[i]*2
                arr[i+1]=0
        res=[num for num in arr if num!=0]
        res+=[0]* (n-len(res))
        return res


arr = [2, 2, 0, 4, 0, 8]
print(Solution().modifyAndRearrangeArr(arr))