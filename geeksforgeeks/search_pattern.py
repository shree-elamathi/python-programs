class solution:
    def search(self,pat,txt):
        ans = []
        txt="0"+txt
        if pat not in txt:
            return ans
        elif pat==txt:
            ans.append(1)
            return ans
        i=0
        j=len(pat)
        while i<len(txt) and j<=len(txt):
            if txt[i:j]==pat:
                ans.append(i)
                i=j
                j=i+len(pat)
            else:
                i=i+1
                j=j+1
        return ans

txt="ababd"
pat="ababd"
print(solution().search(pat,txt))