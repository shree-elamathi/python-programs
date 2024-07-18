'''
You are given an array arr. Your task is to find the longest length of a good sequence. A good sequence {x1, x2, .. xn}
is an alternating sequence if its elements satisfy one of the following relations :
'''
class Solution:
    def alternatingMaxLength(self, arr):
        incre=1
        decre=1
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                incre=decre+1
            elif arr[i]<arr[i-1]:
                decre=incre+1
        return max(incre,decre)

arr= [1, 5, 4]
print(Solution().alternatingMaxLength(arr))