#Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of
# the string after removal of k characters. The value of a string is defined as the sum of squares of
# the count of each distinct character present in the string.
class solution:
    def minvalue(self,s,k):
        let=[]
        count=[]
        val=0
        for i in s:
            if i not in let:
                let.append(i)
        for j in let:
            count.append(s.count(j))
        count.sort()
        while k!=0:
            x=max(count)
            y=count.index(x)
            count[y]=x-1
            k=k-1
        for i in count:
            val=val+(i*i)
        return val

s="abccc"
k=1
print(solution().minvalue(s,k))