'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters
can be different.
'''

class Solution:
    def groupAnagrams(self, strs):
        def isAnagram(s: str, t: str) -> bool:
            hashs = [0] * 26
            hasht = [0] * 26

            if len(s) != len(t):
                return False

            for char in s:
                hashs[ord(char) - 97] += 1

            for char in t:
                hasht[ord(char) - 97] += 1

            for char in s:
                if hashs[ord(char) - 97] != hasht[ord(char) - 97]:
                    return False

            return True

        ans = []
        vis = [ 0 ] * len(strs)
        for i in range(len(strs)):
            if vis[i] != 1:
                temp= []
                temp.append(strs[i])
                vis[i] = 1
                for j in range(i+1, len(strs)):
                    if isAnagram(strs[i],strs[j]):
                        temp.append(strs[j])
                        vis[j] = 1
                ans.append(temp)
        return ans


strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))
