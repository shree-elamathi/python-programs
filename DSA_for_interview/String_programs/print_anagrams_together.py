'''
Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be
arranged in the order of their appearance in the original array. Refer to the sample case for clarification.
'''

class Solution:
    def areAnagrams(self, s1, s2):
        hashs1 = [0] * 26
        hashs2 = [0] * 26
        if len(s1) < len(s2):
            return False

        for char in s1:
            hashs1[ord(char) - 97] += 1

        for char in s2:
            hashs2[ord(char) - 97] += 1

        for char in s1:
            if hashs1[ord(char) - 97] != hashs2[ord(char) - 97]:
                return False
        return True
    def anagrams(self, arr):
        new_arr = [0] * len(arr)
        ans = []
        for i in range(len(arr)):
            res = [arr[i]]
            if new_arr[i] !=-1:
                for j in range(i + 1, len(arr)):
                    if  len(arr[i]) == len(arr[j]):
                        if self.areAnagrams(arr[i], arr[j]):
                            new_arr[i] = -1
                            new_arr[j] = -1
                            res.append(arr[j])
                ans.append(res)
        return ans


arr= ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(Solution().anagrams(arr))
