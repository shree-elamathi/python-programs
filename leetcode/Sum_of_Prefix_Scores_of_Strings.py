'''
You are given an array words of size n consisting of non-empty strings.
We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab"
and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
Note that a string is considered as a prefix of itself.
'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
            node.count+=1
    def get_prefix_score(self,word):
        node=self.root
        score_sum=0
        for char in word:
            if char in node.children:
                node=node.children[char]
                score_sum+=node.count
        return score_sum
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()
        for word in words:
            trie.insert(word)
        answer=[]
        for word in words:
            score=trie.get_prefix_score(word)
            answer.append(score)
        return answer