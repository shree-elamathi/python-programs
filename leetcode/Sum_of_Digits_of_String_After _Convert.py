'''
You are given a string s consisting of lowercase English letters, and an integer k.
First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with
1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the
transform operation k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
'''
class Solution:
    def getLucky(self, s, k):
        dict=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        arr=[]
        for letter in s:
            x=str(dict.index(letter)+1)
            for i in x:
                arr.append(int(i))
        while k>0:
            x=str(sum(arr))
            arr.clear()
            for i in x:
                arr.append(int(i))
            k-=1
        res=""
        for i in arr:
            res+=str(i)
        return int(res)


s = "leetcode"
k = 2
print(Solution().getLucky(s,k))