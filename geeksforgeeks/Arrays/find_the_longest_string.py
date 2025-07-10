'''
Given an array of strings words[]. Find the longest string in words[] such that every prefix of it is also
present in the array words[].
Note: If multiple strings have the same maximum length, return the lexicographically smallest one.
'''

class Solution():
    def longestString(self, words):
        # approach -> 1
        Hashmap = {}
        words.sort(key=len)
        res = []
        for word in words:
            val = 0
            for i in range(len(word)):
                if word[:i + 1] in Hashmap:
                    val += 1
                else:
                    Hashmap[word] = 1
                    break
            if val == len(word) - 1:
                res.append(word)
        res.sort()
        val = res[0]
        for word in res:
            if len(word) > len(val):
                val = word
        return val

    # approach -> 2
    # Dict = {}
    # ans =""
    # for i in words:
    #     Dict[i] = 1
    # for word in words:
    #     s = ''
    #     l = len(word)
    #     for j in range(l):
    #         s += word[j]
    #         if Dict.get(s,0) == 0:
    #             l = 0
    #             break
    #     l_ans = len(ans)
    #     if l_ans<=1:
    #         if l_ans == 1:
    #             ans = min(ans, word)
    #         else:
    #             ans = word
    # return ans



words = ["qho", "q", "qhw", "qh", "v", "qo"]
print(Solution().longestString(words))