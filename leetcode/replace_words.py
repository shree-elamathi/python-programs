'''
In English, we have a concept called root, which can be followed by some other word to form another
longer word - let's call this word derivative. For example, when the root "help" is followed by the word
"ful", we can form a derivative "helpful". Given a dictionary consisting of many roots and a sentence
consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it.
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.
Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
'''
class Solution:
    def rep_word(self,dictionary,sentence):
        sen=[]
        word=""
        res=""
        for i in sentence:
            if i==" ":
                sen.append(word)
                word=""
            else:
                word+=i
        sen.append(word)
        dictionary=sorted(dictionary,key=len)
        for i in dictionary:
            for j in range(len(sen)):
                wor=sen[j]
                if i==wor[:len(i)]:
                    sen[j]=i
        for i in sen:
            res+=i+" "
        return res[:len(res)-1]
dictionary=["a","b","c"]
sentence="aadsfasf absbs bbab cadsfafs"
print(Solution().rep_word(dictionary,sentence))

