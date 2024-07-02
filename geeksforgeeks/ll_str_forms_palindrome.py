'''
Given a linked list with string data, check whether the combined string formed is palindrome. If the
combined string is palindrome then return true otherwise return false.
'''
class Solution:
    def compute(self,head):
        word="hello"
        #while head:
         #   word+=head.data
          #  head=head.data
        rev_word=word[::-1]
        if word==rev_word:
            return True
        else:
            return False

print(Solution().compute(3))