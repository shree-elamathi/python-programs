s= "aaaabbaa"

class Solution:
    def isPalaindrome(self, word):
        new_word = word[::-1]
        if new_word == word:
            return True
        return False
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        res = []
        ind = 0
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    word = s[i:j+1]
                    if self.isPalaindrome(word):
                        res.append(word)
                        if len(word) > max_len:
                            max_len = len(word)
                            ind = res.index(word)
        return res[ind]
              

print(Solution().longestPalindrome(s))
                  
            
        
        
