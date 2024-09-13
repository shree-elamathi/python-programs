'''
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti,
righti].
For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR
arr[righti] ).
Return an array answer where answer[i] is the answer to the ith query.
'''
class Solution:
    def xorQueries(self, arr, queries):
        prefix_xor=[0]*(len(arr)+1)
        for i in range(len(arr)):
            prefix_xor[i+1]=prefix_xor[i]^arr[i]
        res=[]
        for query in queries:
            res.append(prefix_xor[query[1] + 1] ^ prefix_xor[query[0]])
        return res