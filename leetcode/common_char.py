'''
Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.
'''
class Solution:
    def commonchar(self,words):
        letter=[]
        w=words[0]
        words.remove(w)
        count=0
        for let in w:
            for i in range(len(words)):
                if let in words[i]:
                    words[i]=words[i].replace(let,"",1)
                    count+=1
            if count==len(words):
                letter.append(let)
                count=0
            else:
                count=0
        return letter
words=["bella","label","roller"]
print(Solution().commonchar(words))
