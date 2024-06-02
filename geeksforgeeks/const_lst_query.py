'''Given a list s that initially contains only a single value 0. There will be q queries of the following types:

0 x: Insert x in the list
1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given q queries.'''
class solution:
    def con_lst(self,q,queries):
        nlst=[0]
        for query in queries:
            if query[0]==0:
                nlst.append(query[1])
            else:
                x=query[1]
                nlst=[a^x for a in nlst]
        return sorted(nlst)



q=3
lst=[[0,2],[1,3],[0,5]]
print(solution().con_lst(q,lst))